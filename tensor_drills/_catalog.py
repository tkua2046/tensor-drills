"""Read and filter the drill metadata in a practice workspace."""

import json
from collections import defaultdict
from pathlib import Path

from . import _DRILL_ID


SCOPES = ("atomic", "composite")
TASK_TYPES = ("create", "debug")
WORKLOADS = range(1, 6)


def describe_drills(
    workspace, *, library=None, scope=None, task_type=None, topics=(), workload=None
):
    root = Path(workspace).resolve() / "drills"
    if not root.is_dir():
        raise ValueError(
            f"No drills directory at {root}. Run tensor-drills init or pass --workspace."
        )

    requested_topics = set(topics)
    matches = []
    prepares_for = defaultdict(set)
    for path in sorted(root.glob("*/*/metadata.json")):
        drill_id = path.parent.relative_to(root).as_posix()
        if not _DRILL_ID.fullmatch(drill_id):
            continue
        selected_library = library is None or path.parent.parent.name == library

        try:
            metadata = _read_metadata(path)
        except (OSError, ValueError) as error:
            if not selected_library:
                continue
            detail = str(error)
            if isinstance(error, json.JSONDecodeError):
                detail = f"invalid JSON ({detail})"
            raise ValueError(f"{path}: {detail}") from error

        for prerequisite in metadata["prerequisites"]:
            practice_drill = prerequisite.get("practice_drill")
            if practice_drill is not None:
                prepares_for[practice_drill].add(drill_id)

        if not selected_library:
            continue
        if scope is not None and metadata["scope"] != scope:
            continue
        if task_type is not None and metadata["task_type"] != task_type:
            continue
        if workload is not None and metadata["workload"] != workload:
            continue
        if not requested_topics.issubset(metadata["topics"]):
            continue
        matches.append((drill_id, metadata))

    return [
        _describe_drill(drill_id, metadata, sorted(prepares_for.get(drill_id, ())))
        for drill_id, metadata in matches
    ]


def _read_metadata(path):
    metadata = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(metadata, dict):
        raise ValueError("expected a JSON object")

    for key, choices in (("scope", SCOPES), ("task_type", TASK_TYPES)):
        if metadata.get(key) not in choices:
            raise ValueError(f"{key} must be one of {', '.join(choices)}")

    workload = metadata.get("workload")
    if isinstance(workload, bool) or workload not in WORKLOADS:
        raise ValueError("workload must be an integer from 1 to 5")
    if not _has_text(metadata.get("goal")):
        raise ValueError("goal must be nonempty text")

    topics = metadata.get("topics")
    if not isinstance(topics, list) or not all(_has_text(topic) for topic in topics):
        raise ValueError("topics must be a list of nonempty strings")

    prerequisites = metadata.get("prerequisites")
    if not isinstance(prerequisites, list):
        raise ValueError("prerequisites must be a list")
    for item in prerequisites:
        if not isinstance(item, dict) or not _has_text(item.get("capability")):
            raise ValueError("each prerequisite must have a nonempty capability")
        if "practice_drill" in item:
            drill_id = item["practice_drill"]
            if not isinstance(drill_id, str) or not _DRILL_ID.fullmatch(drill_id):
                raise ValueError("practice_drill must be a drill ID in library/name form")
    return metadata


def _has_text(value):
    return isinstance(value, str) and bool(value.strip())


def _describe_drill(drill_id, metadata, prepares_for):
    scope = metadata["scope"]
    task_type = metadata["task_type"]
    workload = int(metadata["workload"])
    lines = [
        f"{drill_id} ({scope} {task_type}, workload {workload})",
        f"  Goal: {metadata['goal']}",
    ]
    if metadata["topics"]:
        lines.append(f"  Topics: {', '.join(metadata['topics'])}")
    for item in metadata["prerequisites"]:
        line = f"  Prerequisite: {item['capability']}"
        if "practice_drill" in item:
            line += f" (practice: {item['practice_drill']})"
        lines.append(line)
    if prepares_for:
        lines.append(f"  Prepares for: {', '.join(prepares_for)}")
    return "\n".join(lines)
