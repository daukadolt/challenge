import base64
from enum import Enum
import json
import mimetypes
from pathlib import Path
from baml_py import Audio, Image, Pdf, Video
from baml_client import b
from baml_client.types import (
    Control,
    EvidenceInput,
    EvidenceType,
    RuleEvaluation,
    RuleStatus,
    RuleType,
)
from typing import List, TypedDict, Dict
import filetype


class EvidenceAnalysis(TypedDict):
    filename: str
    result: List[RuleEvaluation]


class _Status(Enum):
    PASS = 0
    FAIL = 1
    MISSING_EVIDENCE = 2
    NOT_APPLICABLE = 3


class SampleReport(TypedDict):
    status: _Status
    report_text: str


def _reconciliate_rules(
    sample_dir: Path,
    evaluation_results: List[RuleEvaluation],
    control: Control,
    aggregated_facts: List[str],
) -> SampleReport:
    output_lines = []

    # Map rule_id to its evaluation
    rule_eval_map = {r.rule_id: r for r in evaluation_results}
    reconciled: Dict[str, _Status] = {}
    rule_defs = {r.id: r for r in control.rules}

    for rule_id, rule_def in rule_defs.items():
        evaluation = rule_eval_map.get(rule_id)

        if evaluation:
            if evaluation.status == RuleStatus.FAIL:
                reconciled[rule_id] = _Status.FAIL
            elif evaluation.status == RuleStatus.PASS:
                reconciled[rule_id] = _Status.PASS
            elif evaluation.status == RuleStatus.MORE_INFOMATION_NEEDED:
                if rule_def.type == RuleType.Blocking:
                    reconciled[rule_id] = _Status.MISSING_EVIDENCE
                else:
                    reconciled[rule_id] = _Status.NOT_APPLICABLE
            else:
                reconciled[rule_id] = _Status.NOT_APPLICABLE
        else:
            # No evaluation returned for this rule
            if rule_def.type == RuleType.Blocking:
                reconciled[rule_id] = _Status.MISSING_EVIDENCE
            else:
                reconciled[rule_id] = _Status.NOT_APPLICABLE

    final_statuses = set(reconciled.values())

    if _Status.FAIL in final_statuses:
        status = _Status.FAIL
    elif _Status.MISSING_EVIDENCE in final_statuses:
        status = _Status.FAIL
    elif _Status.PASS in final_statuses:
        status = _Status.PASS
    else:
        status = _Status.NOT_APPLICABLE

    output_lines.append("# Audit Sample Report")
    output_lines.append(f"**Overall Status:** {status.name}\n")

    output_lines.append("## Rule Reconciliation Summary")
    output_lines.append("| Rule ID | Type | Verdict | Reason |")
    output_lines.append("| :--- | :--- | :--- | :--- |")

    for rule_id, verdict in reconciled.items():
        r_type = rule_defs[rule_id].type if rule_id in rule_defs else "Unknown"
        evaluation = rule_eval_map.get(rule_id)
        reason = evaluation.reasoning if evaluation else "No evaluation generated"

        if verdict == _Status.MISSING_EVIDENCE and not evaluation:
            reason = "Blocking rule applied but no passing evidence found in sample."

        reason_short = (reason[:100] + "...") if len(reason) > 100 else reason

        output_lines.append(
            f"| {rule_id} | {r_type} | {verdict.name} | {reason_short} |"
        )

    output_lines.append("\n## Detailed Evidence Logs")

    if aggregated_facts:
        output_lines.append(f"Total Evidence Items Processed: {len(aggregated_facts)}")
        for idx, fact_str in enumerate(aggregated_facts, 1):
            try:
                fact_json = json.loads(fact_str)
                source = fact_json.get("_source", "Unknown")
                output_lines.append(f"\n### Evidence [{idx}]: {source}")
                output_lines.append("```json")
                output_lines.append(json.dumps(fact_json, indent=2))
                output_lines.append("```")
            except:
                output_lines.append(f"\n### Evidence [{idx}]")
                output_lines.append(fact_str)
    else:
        output_lines.append("(No evidence extracted from files)")

    combined_output = "\n".join(output_lines)

    output_file = sample_dir / "audit_results.md"
    with open(output_file, "w") as f:
        f.write(combined_output)

    return {"status": status, "report_text": combined_output}


def get_mime_and_category(file_path: Path):
    """
    Returns tuple: (mime_type, category_key)
    category_key is one of: 'image', 'pdf', 'audio', 'video', 'text', or None
    """
    kind = filetype.guess(str(file_path))

    if kind:
        mime = kind.mime
        if mime == "application/pdf":
            return mime, "pdf"
        if mime.startswith("image/"):
            return mime, "image"
        if mime.startswith("video/"):
            return mime, "video"
        if mime.startswith("audio/"):
            return mime, "audio"

    mime, _ = mimetypes.guess_type(file_path)

    if mime:
        if mime.startswith("text/") or mime in ["application/json", "application/xml"]:
            return mime, "text"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read(1024)  # Read first 1kb
        return "text/plain", "text"
    except UnicodeDecodeError:
        return None, None


def process_sample(sample_dir: Path, control: Control) -> None:
    print(f"Processing {sample_dir}")

    all_files = sorted([f for f in sample_dir.iterdir() if not f.name.startswith(".")])
    aggregated_facts: List[str] = []

    # Phase 1: Extract from all files
    for file_path in all_files:
        if file_path.is_dir():
            continue

        if file_path.name == "audit_results.md":
            continue

        try:
            print(f"  Analyzing {file_path.name}...")

            mime_type, category = get_mime_and_category(file_path)
            ev_input = EvidenceInput()

            if category == "image":
                with open(file_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                ev_input.img = Image.from_base64(mime_type, encoded)

            elif category == "pdf":
                with open(file_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                ev_input.pdf_file = Pdf.from_base64(encoded)

            # TODO: this'll need more support

            # elif category == "audio":
            #     with open(file_path, "rb") as f:
            #         encoded = base64.b64encode(f.read()).decode("utf-8")
            #     ev_input.audio_file = Audio.from_base64(mime_type, encoded)

            # elif category == "video":
            #     with open(file_path, "rb") as f:
            #         encoded = base64.b64encode(f.read()).decode("utf-8")
            #     ev_input.video_file = Video.from_base64(mime_type, encoded)

            elif category == "text":
                # errors='replace' is safer for logs with weird characters
                ev_input.text = file_path.read_text(encoding="utf-8", errors="replace")

            else:
                print(f"    Skipping unknown file type: {file_path.name}")
                continue

            evidence_type = b.IdentifyEvidenceType(input=ev_input)

            facts_model = None
            if evidence_type == EvidenceType.CIPipeline:
                facts_model = b.ExtractCIFacts(input=ev_input)
            elif evidence_type == EvidenceType.CoverageReport:
                facts_model = b.ExtractCoverageFacts(input=ev_input)
            elif evidence_type == EvidenceType.PullRequest:
                facts_model = b.ExtractPRFacts(input=ev_input)
            elif evidence_type == EvidenceType.TestResult:
                facts_model = b.ExtractTestResultFacts(input=ev_input)
            elif evidence_type == EvidenceType.SecurityScan:
                facts_model = b.ExtractSecurityFacts(input=ev_input)
            elif evidence_type == EvidenceType.IssueBoard:
                facts_model = b.ExtractIssueBoardFacts(input=ev_input)
            elif evidence_type == EvidenceType.PerformanceReport:
                facts_model = b.ExtractPerformanceFacts(input=ev_input)
            elif evidence_type == EvidenceType.GitCommit:
                facts_model = b.ExtractCommitFacts(input=ev_input)

            if facts_model:
                data = facts_model.model_dump()
                data["_source"] = file_path.name
                aggregated_facts.append(json.dumps(data))
            else:
                print(f"    No extractor for {evidence_type} on {file_path.name}")

        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

    # Phase 2: Evaluate Once
    if aggregated_facts:
        print("  Evaluating aggregated facts against control policy...")
        results = b.EvaluateCompliance(aggregated_facts, control)
        report = _reconciliate_rules(sample_dir, results, control, aggregated_facts)
        print(f"Sample Result: {report['status'].name}")
    else:
        print("  No facts extracted, skipping evaluation.")
