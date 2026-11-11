"""Load a drill manifest and execute its verifier in a child process."""

import importlib
import json
import runpy
import sys
from pathlib import Path


class AttemptError(Exception):
    """A candidate function could not complete a case."""


def read_manifest(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    dependencies = data["dependencies"]
    cases = data["cases"]
    if not isinstance(dependencies, list) or any(
        not isinstance(name, str) or not name for name in dependencies
    ):
        raise ValueError("dependencies must be a list of module names")
    if not isinstance(cases, list) or not cases:
        raise ValueError("the manifest must contain at least one case")
    names = set()
    for case in cases:
        name = case["name"]
        if not isinstance(name, str) or not name or name in names:
            raise ValueError("case names must be nonempty and unique")
        if "inputs" not in case or "expected" not in case:
            raise ValueError(f"{name} must supply inputs and expected results")
        names.add(name)
    return dependencies, cases


def setup_error(error):
    print(f"SETUP ERROR {type(error).__name__}: {error}", file=sys.stderr)
    return 2


def run(drill, package, attempt):
    try:
        dependencies, cases = read_manifest(package / "tests.json")
        for dependency in dependencies:
            importlib.import_module(dependency)
        sys.path.insert(0, str(drill))
        verifier = package / "verify.py"
        if not verifier.is_file():
            verifier = drill / "verify.py"
        check_case = runpy.run_path(str(verifier))["check_case"]
        if not callable(check_case):
            raise TypeError("verify.py must define a callable check_case")
    except (Exception, SystemExit) as error:
        return setup_error(error)

    try:
        namespace = runpy.run_path(str(attempt))
    except (Exception, SystemExit) as error:
        print(f"FAIL loading attempt: {type(error).__name__}: {error}")
        return 1

    def call(name, *args, **kwargs):
        function = namespace.get(name)
        if not callable(function):
            raise AttemptError(f"Define the function {name} in the attempt.")
        try:
            return function(*args, **kwargs)
        except (Exception, SystemExit) as error:
            raise AttemptError(f"{name} raised {type(error).__name__}: {error}") from error

    failures = 0
    for case in cases:
        name = case["name"]
        try:
            check_case(call, case["inputs"], case["expected"])
        except (AssertionError, AttemptError) as error:
            print(f"FAIL {name}" + (f": {error}" if str(error) else ""))
            failures += 1
        except (Exception, SystemExit) as error:
            return setup_error(error)
        else:
            print(f"PASS {name}")
    print(f"{len(cases) - failures}/{len(cases)} cases passed")
    return int(failures > 0)


if __name__ == "__main__":
    sys.exit(run(*(Path(path) for path in sys.argv[1:])))
