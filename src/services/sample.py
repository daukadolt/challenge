import base64
import json
from pathlib import Path
from baml_py import Image
from baml_client import b
from baml_client.types import Control, EvidenceType, RuleEvaluation
from typing import List, TypedDict


class EvidenceAnalysis(TypedDict):
    filename: str
    result: List[RuleEvaluation]


def process_sample(sample_dir: Path, control: Control) -> None:
    print(f"Processing {sample_dir}")
    image_files = sorted(sample_dir.glob("*.png"))

    results: List[EvidenceAnalysis] = []

    for image_path in image_files:
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        img = Image.from_base64("image/png", encoded)
        evidence_type = b.IdentifyEvidenceType(img=img)

        if evidence_type == EvidenceType.CIPipeline:
            facts = b.ExtractCIFacts(img=img)
            facts_str = json.dumps(facts.model_dump(), indent=2)
        elif evidence_type == EvidenceType.CoverageReport:
            facts = b.ExtractCoverageFacts(img=img)
            facts_str = json.dumps(facts.model_dump(), indent=2)
        elif evidence_type == EvidenceType.PullRequest:
            facts = b.ExtractPRFacts(img=img)
            facts_str = json.dumps(facts.model_dump(), indent=2)
        else:
            facts_str = ""

        res = b.EvaluateCompliance(facts_str, control)

        results.append({"filename": image_path.name, "result": res})

    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append("COMBINED RESULTS")
    output_lines.append("=" * 80)

    for idx, result in enumerate(results, 1):
        output_lines.append(f"\n[{idx}] {result['filename']}")
        output_lines.append("-" * 80)
        result_data = [r.model_dump() for r in result["result"]]
        result_json = json.dumps(result_data, indent=2)
        output_lines.append(result_json)

    combined_output = "\n".join(output_lines)

    print("\n" + combined_output)

    output_file = sample_dir / "results.txt"
    with open(output_file, "w") as f:
        f.write(combined_output)
