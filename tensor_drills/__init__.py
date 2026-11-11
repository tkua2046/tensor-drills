"""Create a tensor drill workspace and check learner attempts."""

import os
import re
import shutil
import subprocess
import sys
from importlib.resources import as_file, files
from pathlib import Path


__all__ = ["check", "init_workspace"]
CHECK_TIMEOUT = 30
_DRILL_ID = re.compile(r"[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*")


def init_workspace(directory: str | Path) -> Path:
    """Copy the bundled drills into a new, editable workspace."""
    destination = Path(directory).resolve()
    examples = files(__name__).joinpath("examples")
    with as_file(examples) as source:
        return shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )


def check(
    drill_id: str,
    *,
    workspace: str | Path = ".",
    variant: bool = False,
    attempt: str | Path | None = None,
) -> int:
    """Print the fixed test results and return 0 for pass, 1 for failure, or 2 for setup."""
    def setup_error(message):
        print(f"SETUP ERROR: {message}", file=sys.stderr)
        return 2

    if not _DRILL_ID.fullmatch(drill_id):
        return setup_error(f"Invalid drill ID: {drill_id!r}. Use library/name.")
    root = Path(workspace).resolve()
    drill = root / "drills" / drill_id
    if not drill.is_dir():
        return setup_error(f"Unknown drill: {drill_id} in {root}")
    package = drill / "variant" if variant else drill
    if not package.is_dir():
        return setup_error(f"No follow-up variant for {drill_id}.")
    attempt_file = (Path(attempt) if attempt is not None else package / "attempt.py").resolve()
    if not attempt_file.is_file():
        return setup_error(f"Attempt file not found: {attempt_file}")

    worker = Path(__file__).with_name("_worker.py").resolve()
    worker_env = os.environ.copy()
    # Verifiers use assertions to reject incorrect answers.
    worker_env.pop("PYTHONOPTIMIZE", None)
    try:
        result = subprocess.run(
            [
                sys.executable, "-B", "-u", str(worker),
                str(drill), str(package), str(attempt_file),
            ],
            stdin=subprocess.DEVNULL,
            timeout=CHECK_TIMEOUT,
            env=worker_env,
        )
    except subprocess.TimeoutExpired:
        print(f"FAIL check exceeded {CHECK_TIMEOUT} seconds", file=sys.stderr)
        return 1
    except OSError as error:
        return setup_error(str(error))
    if result.returncode in (0, 1, 2):
        return result.returncode
    print(f"FAIL check process ended with status {result.returncode}", file=sys.stderr)
    return 1
