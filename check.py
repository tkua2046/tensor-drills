"""Run the checker against the bundled practice drills."""

import sys
from pathlib import Path

from tensor_drills.cli import main


if __name__ == "__main__":
    practice = Path(__file__).resolve().parent / "tensor_drills" / "practice"
    sys.exit(main(["check", *sys.argv[1:]], default_workspace=practice))
