"""Run the checker against the bundled source examples."""

import sys
from pathlib import Path

from tensor_drills.cli import main


if __name__ == "__main__":
    examples = Path(__file__).resolve().parent / "tensor_drills" / "examples"
    sys.exit(main(["check", *sys.argv[1:]], default_workspace=examples))
