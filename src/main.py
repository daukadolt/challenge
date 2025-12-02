import argparse
from dotenv import load_dotenv
from pathlib import Path

from services import control as control_service
from services import sample as sample_service

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="Process independent code review samples."
    )
    parser.add_argument(
        "control_dir",
        type=Path,
        nargs="?",
        default="data/independent-code-review",
        help="Path to the control directory containing control MD files and samples",
    )
    args = parser.parse_args()

    control_dir = Path(args.control_dir)
    if not control_dir.is_dir():
        raise NotADirectoryError(f"Control directory is not a directory: {control_dir}")

    samples_dir = control_dir / "samples"
    if not samples_dir.exists():
        raise FileNotFoundError(f"Samples directory does not exist: {samples_dir}")

    control = control_service.init_control(control_dir)

    for item in samples_dir.iterdir():
        if item.is_dir():
            sample_service.process_sample(item, control)


if __name__ == "__main__":
    main()
