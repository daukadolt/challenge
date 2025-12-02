from dotenv import load_dotenv
import base64
import asyncio
import json
from pathlib import Path
from baml_py import Image
from baml_client import b
from baml_client.types import Control, EvidenceType, RuleEvaluation
from typing import List, TypedDict

load_dotenv()


class EvidenceAnalysis(TypedDict):
    filename: str
    result: List[RuleEvaluation]


def init_control(control_dir: Path) -> Control:
    control_file = control_dir / "control.json"

    if control_file.exists():
        print("Loading control from control.json...")
        from baml_client.types import Control

        with open(control_file, "r") as f:
            control_dict = json.load(f)
        control = Control(**control_dict)
        print(f"Loaded {len(control.rules)} rules from cache")
        return control

    md_files = sorted(control_dir.glob("*.md"))

    combined_content = []

    for file_path in md_files:
        print(f"Reading: {file_path.name}")
        content = file_path.read_text(encoding="utf-8")
        combined_content.append(content)
        combined_content.append("\n\n---\n\n")

    control_text = "".join(combined_content)

    print("Extracting control structure...")
    control = b.ExtractControl(control_text)

    # Save to JSON using Pydantic's model_dump
    with open(control_file, "w") as f:
        json.dump(control.model_dump(), f, indent=2)

    print(f"Saved {len(control.rules)} rules to control.json")

    return control


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


async def main():
    control_dir = Path("data/independent-code-review")

    control = init_control(control_dir)

    samples_dir = control_dir / "samples"

    for item in samples_dir.iterdir():
        if item.is_dir():
            process_sample(item, control)


if __name__ == "__main__":
    asyncio.run(main())
