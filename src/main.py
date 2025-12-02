from dotenv import load_dotenv
from pathlib import Path

from services import control as control_service
from services import sample as sample_service

load_dotenv()


def main():
    control_dir = Path("data/independent-code-review")

    control = control_service.init_control(control_dir)

    samples_dir = control_dir / "samples"

    for item in samples_dir.iterdir():
        if item.is_dir():
            sample_service.process_sample(item, control)


if __name__ == "__main__":
    main()
