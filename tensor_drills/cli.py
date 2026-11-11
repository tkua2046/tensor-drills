"""Set up, find, and run NumPy and PyTorch interview drills."""

import argparse
import sys
from pathlib import Path

from . import check, init_workspace
from ._catalog import SCOPES, TASK_TYPES, WORKLOADS, describe_drills


def main(argv=None, *, default_workspace="."):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="copy the bundled drills into a new workspace")
    init.add_argument("directory", type=Path)

    catalog = commands.add_parser("list", help="list drills by catalog metadata")
    catalog.add_argument("--workspace", type=Path, default=default_workspace, help="workspace root")
    catalog.add_argument("--library", type=str.lower, help="library name, such as numpy or pytorch")
    catalog.add_argument("--scope", choices=SCOPES, help="drill scope")
    catalog.add_argument("--task-type", choices=TASK_TYPES, help="drill task type")
    catalog.add_argument("--topic", action="append", default=[], help="require this topic (repeatable)")
    catalog.add_argument("--workload", type=int, choices=WORKLOADS, help="exact workload rating")

    run = commands.add_parser("check", help="run the fixed tests for a drill")
    run.add_argument("drill_id", metavar="library/name")
    run.add_argument("--workspace", type=Path, default=default_workspace, help="workspace root")
    run.add_argument("--variant", action="store_true", help="check a variant in an existing workspace")
    run.add_argument("--attempt", type=Path, help="check a saved Python file")
    args = parser.parse_args(argv)

    if args.command == "init":
        try:
            workspace = init_workspace(args.directory)
        except FileExistsError:
            parser.error(f"Workspace already exists: {args.directory}. Choose a new directory.")
        except OSError as error:
            parser.error(str(error))
        print(f"Created {workspace}. Open its README.md to choose a drill.")
        return 0

    if args.command == "list":
        try:
            entries = describe_drills(
                args.workspace,
                library=args.library,
                scope=args.scope,
                task_type=args.task_type,
                topics=args.topic,
                workload=args.workload,
            )
        except (OSError, ValueError) as error:
            print(f"SETUP ERROR: {error}", file=sys.stderr)
            return 2
        print("\n\n".join(entries) if entries else "No drills match.")
        return 0

    return check(
        args.drill_id, workspace=args.workspace, variant=args.variant, attempt=args.attempt
    )


if __name__ == "__main__":
    sys.exit(main())
