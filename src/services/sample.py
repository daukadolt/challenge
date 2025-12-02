import base64
from enum import Enum
import json
from pathlib import Path
from baml_py import Image
from baml_client import b
from baml_client.types import (
    Control,
    EvidenceType,
    RuleEvaluation,
    RuleStatus,
    RuleType,
)
from typing import List, TypedDict, Dict


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
    sample_dir: Path, evidence_results: List[EvidenceAnalysis], control: Control
) -> SampleReport:
    output_lines = []

    rule_map: Dict[str, List[RuleEvaluation]] = {}
    for result in evidence_results:
        for r in result["result"]:
            if r.rule_id not in rule_map:
                rule_map[r.rule_id] = []
            rule_map[r.rule_id].append(r)

    reconciled: Dict[str, _Status] = {}

    rule_defs = {r.id: r for r in control.rules}

    for rule_id, evals in rule_map.items():
        statuses = {e.status for e in evals}
        rule_def = rule_defs.get(rule_id)

        if RuleStatus.FAIL in statuses:
            reconciled[rule_id] = _Status.FAIL

        elif RuleStatus.PASS in statuses:
            reconciled[rule_id] = _Status.PASS

        else:
            if rule_def and rule_def.type == RuleType.Blocking:
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
        reasons = [
            e.reasoning for e in rule_map[rule_id] if e.status == RuleStatus.FAIL
        ]
        if not reasons and verdict == _Status.PASS:
            reasons = ["Validated via evidence"]
        elif verdict == _Status.MISSING_EVIDENCE:
            reasons = ["Blocking rule applied but no passing evidence found in sample."]

        if reasons:
            reason_short = (
                (reasons[0][:100] + "...") if len(reasons[0]) > 100 else reasons[0]
            )
        else:
            reason_short = "No Data"

        output_lines.append(
            f"| {rule_id} | {r_type} | {verdict.name} | {reason_short} |"
        )

    output_lines.append("\n## Detailed Evidence Logs")
    for idx, result in enumerate(evidence_results, 1):
        output_lines.append(f"\n### Evidence [{idx}]: {result['filename']}")
        relevant_results = [r.model_dump() for r in result["result"]]
        if relevant_results:
            output_lines.append("```json")
            output_lines.append(json.dumps(relevant_results, indent=2))
            output_lines.append("```")
        else:
            output_lines.append("(No relevant compliance signals found in this file)")

    combined_output = "\n".join(output_lines)

    output_file = sample_dir / "audit_results.md"
    with open(output_file, "w") as f:
        f.write(combined_output)

    return {"status": status, "report_text": combined_output}


def process_sample(sample_dir: Path, control: Control) -> None:
    print(f"Processing {sample_dir}")
    image_files = sorted(sample_dir.glob("*.png"))

    results: List[EvidenceAnalysis] = []

    for image_path in image_files:
        try:
            print(f"  Analyzing {image_path.name}...")
            with open(image_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")

            img = Image.from_base64("image/png", encoded)
            evidence_type = b.IdentifyEvidenceType(img=img)

            facts_str = ""
            if evidence_type == EvidenceType.CIPipeline:
                facts_str = json.dumps(b.ExtractCIFacts(img=img).model_dump())
            elif evidence_type == EvidenceType.CoverageReport:
                facts_str = json.dumps(b.ExtractCoverageFacts(img=img).model_dump())
            elif evidence_type == EvidenceType.PullRequest:
                facts_str = json.dumps(b.ExtractPRFacts(img=img).model_dump())

            if facts_str:
                res = b.EvaluateCompliance(facts_str, control)
                results.append({"filename": image_path.name, "result": res})
            else:
                print(
                    f"    Skipping compliance check for {image_path.name} (Type: {evidence_type})"
                )

        except Exception as e:
            print(f"Error processing {image_path.name}: {e}")

    report = _reconciliate_rules(sample_dir, results, control)
    print(f"Sample Result: {report['status'].name}")
