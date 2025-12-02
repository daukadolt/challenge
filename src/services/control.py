import json
from pathlib import Path
from baml_client import b
from baml_client.types import Control


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

    if len(md_files) == 0:
        raise Exception(
            "No markdown files present in the root folder of the control, aborting..."
        )

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
