# Drill Authoring Guide

Use the delivery sequence and authoring brief for your track when adding a bundled drill. When an outcome is shared, use the same brief for NumPy and PyTorch. [Content implementation plan](CONTENT_IMPLEMENTATION_PLAN.md)

## Review the brief

When a plausible mistake could pass an obvious example, ask a reviewer to work through the brief before writing the drill. Give them the intended learning outcome and ask for three things.

1. **Clarify the contract.** State what the learner should demonstrate and flag any missing assumption that changes which solutions are valid. For arithmetic tasks, check that the dtype, numeric domain, and error allowance admit the intended native operations, including cancellation and underflow.
2. **Find a case that exposes a mistake.** Name a plausible wrong approach and give a small input that separates it from correct behavior. Record the expected result or state change and what the wrong approach would do. For a debug drill, identify the symptom the starter should reproduce.
3. **Decide how to assess it.** Say what a fixed check can observe and what the rubric should ask the learner to demonstrate in their code or explanation. Keep room for equivalent valid approaches.

For shared briefs, check whether the same case exposes the mistake in each library. Give the author the contract questions and proposed cases, then revisit them when reviewing the completed drill.

Use a small evidence table when a drill combines requirements. It can stay in the review notes; it is not another drill file.

| Requirement from the prompt | Input or state that exercises it | Plausible mistake | Evidence |
| --- | --- | --- | --- |
| Include equal query/key positions in causal attention | Both positions are valid and the equal-position key affects the result | Use `<` instead of `<=` | A named fixed case distinguishes values or gradients. |
| Use a custom backward | A nonuniform upstream gradient reaches the supplied input | Use ordinary native composition | Fixed values and gradients check correctness; the rubric inspects actual custom Function participation. |

Keep fixture inputs inside the published contract. A boundary only counts as exercised when it can affect the checked result: an equality hidden by padding does not test the inclusive comparison.

For integer comparisons or searches that accept the full int64 range, include adjacent large values as well as opposite extremes. A conversion to floating point can preserve the order of the extremes while losing the distinction between nearby integers.

## Start from the template

Use the six files in [drill template](../templates/drill/) for either NumPy or PyTorch. From the repository root, choose an unused ID and copy the files into the bundled catalog. Set `track=pytorch` for a PyTorch drill.

```sh
track=numpy
drill="$track/my-drill"
destination="tensor_drills/practice/drills/$drill"
mkdir "$destination" && cp templates/drill/* "$destination/"
```

For a custom drill, copy the template into `drills/<library>/<name>/` in your practice workspace. Custom drills can run by ID with `tensor-drills check`. Fill in `metadata.json` if you want the drill listed in the catalog. Leave that file out of a custom drill you plan to run only by ID. The template's setup link resolves when the drill is in its workspace folder.

Replace the placeholders in the copied files. Set the banner in `prompt.md` to the drill's library, scope, and task type, such as `PyTorch · Composite debug`. Describe the task, contract, and how to run and submit an attempt. When the drill has `metadata.json`, match the scope, task type, and goal sentence to the prompt. [Learner prompt guidance](INFRA_DESIGN.md#learner-prompt) · [Catalog metadata guidance](INFRA_DESIGN.md#catalog-metadata)

Replace the template's function and fixtures with the drill's actual signature, inputs, and expected results. Each case in `tests.json` has a unique `name`, `inputs`, and `expected` results. List the required imports in `dependencies`, such as `numpy` or `torch`.

The template starts with a create stub. For a debug drill, supply a faulty implementation and update the prompt to describe the observable failure and the expected starter check result. Record the intended bugs and the evidence of each repair in the rubric. [Create example](../tensor_drills/practice/drills/numpy/row-gather/prompt.md) · [Debug example](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) · [Drill format](INFRA_DESIGN.md#drill-package-and-assessment)

In `verify.py`, define `check_case(call, inputs, expected)`. Construct fresh inputs from the case, invoke the learner's function with `call("function_name", ...)`, and raise an assertion with an explanation for an incorrect result. The template shows a scalar comparison. Use array or tensor assertions where appropriate and check shape, dtype, values, and input mutations as required by the contract. [NumPy verifier](../tensor_drills/practice/drills/numpy/row-gather/verify.py) · [PyTorch verifier](../tensor_drills/practice/drills/pytorch/row-gather/verify.py)

Use `rubric.md` to record the evidence a reviewer should look for in the attempt and explanation. Package reusable coding follow-ups as standalone drills and link prerequisite practice when it is available. [Rubric guidance](INFRA_DESIGN.md#reviewer-rubric) · [Follow-up guidance](INFRA_DESIGN.md#optional-follow-ups)

## Verify from a fresh workspace

From the repository root, set `track` to `numpy` or `pytorch` and `drill` to the ID you are checking. Create a temporary environment with Python 3.12 or newer and install the corresponding track.

```sh
scratch="$(mktemp -d)"
uv venv --python 3.12 "$scratch/venv"
uv pip install --python "$scratch/venv/bin/python" ".[${track}]"
runner="$scratch/venv/bin/tensor-drills"

"$runner" init "$scratch/workspace"
```

The bundled drill comes from the installed package. For a custom drill, set `custom_workspace` to the workspace where you authored it and copy the drill into the fresh workspace. Use an ID that is free in the destination.

```sh
custom_workspace=/path/to/your/practice-workspace
mkdir "$scratch/workspace/drills/$drill" &&
    cp -R "$custom_workspace/drills/$drill/." "$scratch/workspace/drills/$drill/"
```

Open the copied prompt and confirm its local links and run instructions work.

### Check catalog metadata and links

Use this step for bundled drills and custom drills with `metadata.json`. If your custom drill has no metadata, go straight to [Check attempts](#check-attempts).

From the repository root, find the drill in the list to confirm discovery. Separately, validate its copied metadata against the [authoring schema](drill-metadata.schema.json) and check that each prerequisite ID resolves in the workspace.

```sh
"$runner" list --workspace "$scratch/workspace" --library "$track"

uv run --no-project --with jsonschema python - "$scratch/workspace" "$drill" <<'PY'
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator

drills = Path(sys.argv[1]) / "drills"
metadata = json.loads((drills / sys.argv[2] / "metadata.json").read_text())
schema = json.loads(Path("docs/drill-metadata.schema.json").read_text())
Draft202012Validator(schema).validate(metadata)

for prerequisite in metadata["prerequisites"]:
    if practice_id := prerequisite.get("practice_drill"):
        target = drills / practice_id
        if not (target / "metadata.json").is_file() or not (target / "prompt.md").is_file():
            raise SystemExit(f"Prerequisite drill is missing from the workspace: {practice_id}")
PY
```

Confirm that the copied prompt's goal matches the metadata. Check that each linked prerequisite practices the capability stated in the metadata.

Reuse the same topic label for the same concept across related drills. Try a relevant `--topic` filter together with `--library` and compare the results with the intended family, including its foundations. Keep distinct concepts, such as matrix products and linear solves, separately labelled.

Use `masks` for Boolean-mask practice, including construction, selection, replacement and assignment. Existing `masking` tags remain as additional labels so that filter continues to work.

### Check attempts

Prepare two materially different valid attempts and plausible wrong attempts in the scratch directory, outside the copied workspace. Choose wrong attempts that target different cases when the drill covers several distinct mistakes. Run the checks from the copied workspace root, as the learner will, and record the exit status and case results of each command.

```sh
(
    cd "$scratch/workspace" || exit 1
    "$runner" check "$drill"
    "$runner" check "$drill" --attempt "$scratch/valid-a.py"
    "$runner" check "$drill" --attempt "$scratch/valid-b.py"
    "$runner" check "$drill" --attempt "$scratch/wrong.py"
)
```

| Attempt | Expected result |
| --- | --- |
| Untouched starter | Exit `1` with the failure described in the prompt. |
| Each valid attempt | Exit `0` with every case passing. |
| Each targeted wrong attempt | Exit `1` with the case that exposes the intended mistake. For each bug assessed by fixed tests, run a partial repair that fixes the other bugs while leaving that bug in place. |

Exit `2` indicates a setup error. Resolve it before interpreting an attempt. Use a separate environment and workspace for the other track when the brief covers both.

## Hand off for review

Give the reviewer the brief, the exact candidate revision or snapshot, and the attempt files or complete steps to recreate them. Record the Python and library versions, commands, and expected and observed exit statuses and case results. Include any limits. Ask the reviewer to check that a learner can start from the prompt and that the fixed cases and rubric assess the stated skill. Send revised files back for recheck when a finding changes the drill.

Use the [content review template](../templates/content-review.md) when it helps record the scope, evidence and follow-up. Keep findings tied to the reviewed revision; accepted curriculum decisions belong in their owning documents. [Review records](reviews/README.md)

### Challenge the assessment

For a new drill, a changed contract or checker, or a delivery assessment audit:

1. **Read the learner materials first.** Form an interpretation from the prompt and starter before consulting the rubric or author solutions. Write an independent valid approach where practical.
2. **Trace the requirements.** Use the evidence table above to check the important boundaries and interactions. Include relevant numeric domains, empty selections, repeated indices, storage relationships, incoming state and backward behavior. Compare fixed fixtures with the prompt's input assumptions.
3. **Try a semantic near miss.** Change one meaningful behavior while preserving the others, such as a denominator, boundary, axis or state transition. Run the saved attempt through the learner CLI. A wrong attempt targeting fixed-test behavior should fail the intended case; accept valid alternatives.
4. **Interpret surviving attempts.** A numerical pass can be appropriate when the prompt and rubric explicitly assess an operation, allocation bound or diagnosis artifact through code and explanation. Report a gap when the combined assessment misses a stated requirement, or when a valid attempt is rejected. General style preferences do not establish failure.
5. **Probe beyond the fixtures.** Use small independent scalar expectations, generated inputs or contract-derived properties where they address a specific risk. Record seeds and domains for generated probes. Keep these review experiments separate from the shipped checker. Turn a useful, deterministic counterexample into a fixed regression case when repairing a defect.

For each finding, preserve the original candidate, attempt, trigger, expected behavior and actual CLI output. Recheck the repair with the original reproducer and valid alternatives, including any other drills that share the affected check. Record the revised candidate and disposition separately from the original finding. State which materials were inspected and which probes were executed; sampling is not an all-catalog runtime check.

When a bundled drill is ready to ship, link it beside its skill and update its source record. [Skill map](SKILL_MAP.md) · [Drill source records](RESOURCES.md#drill-source-records)

## Review the catalog

Review the catalog as a whole when adding a substantial skill family or preparing a content release. This complements per-drill review and can reveal gaps between individually useful exercises.

1. Start from the [fluency goal and selection criteria](CONTENT_DESIGN.md), supported by relevant public references. Assess NumPy and PyTorch separately. The existing map and completed delivery plan are evidence of current choices, not the boundary of useful practice.
2. Inventory the drills by primary outcome and group overlapping families. For each, trace the prompt's goal to a fixed case or rubric criterion, identify assumed capabilities, and state what makes the exercise distinct. Different mutation, denominator, gradient or diagnosis requirements can justify separate drills.
3. Walk through plausible entry and follow-up choices using the actual metadata. Check that prerequisite links teach their stated capability and that topic labels and relative workload help discovery. Distinguish a missing skill from missing standalone practice of a skill already assessed in a composite task.
4. Prioritize meaningful gaps and redundancies by frequency of use, transfer value and consequences of misunderstanding. Suggest strengthening, combining, adding or deferring practice with a reason; avoid a target drill count or a checklist of every library API.

Report assessment defects separately from curriculum recommendations and optional improvements. Cite the drill materials and the learning consequence. An explicit deferral can be reconsidered with evidence. Accepted curriculum decisions belong in the design, skill map and delivery plan; review notes preserve the findings and their disposition. [Document responsibilities](README.md)

## Author and reviewer prompts

### Author prompt

```text
Author <drill IDs> from <brief link or text>. Start with the six files in
templates/drill and follow docs/DRILL_AUTHORING.md. Use the same
outcome for paired tracks. Use docs/README.md to locate any documentation
updates the drill needs.

Use the brief review findings, when available, to settle the contract
and choose cases before authoring the drill.

Write the learner contract and its examples before implementing checks.
Define the accepted shapes, dtypes, scalar bounds, and mutations that matter.
State whether floating inputs must be finite.
Choose cases that distinguish plausible mistakes, including combinations of
allowed inputs that change behavior. Derive expected results from the contract.

If a library operation is part of the skill, say so in the learner prompt
and ask for evidence from the learner's code and explanation in the rubric.
Use fixed checks for observable behavior and allow equivalent approaches.

Follow the verification recipe in docs/DRILL_AUTHORING.md for each affected
track. Return the changed files and the verification attempts or complete
steps to recreate them. Include the Python and library versions, exact
commands, expected and observed exit statuses and case results, and any
remaining limitations.
```

### Reviewer prompt

```text
Review <drill IDs> at <candidate revision or snapshot> against <brief>.
Read the learner materials first. Then compare the contract, fixed cases,
and rubric. Use docs/DRILL_AUTHORING.md to check the fresh workspace flow.

Try a missing boundary case and a plausible solution that passes the fixed
checks while skipping the intended skill. Judge whether the rubric catches
the latter. Check each affected library and report what you actually ran.
Use Challenge the assessment in docs/DRILL_AUTHORING.md. Distinguish a
fixed-test escape covered fairly by the rubric from an assessment defect.
Preserve reproducers and exact outcomes so repairs can be rechecked.

Report findings with file locations, reproductions, and suggested fixes.
For documentation changes, use Editing and review in docs/README.md to
check each document's responsibility and trace changed claims to their
source.
Review the candidate read-only and run experiments in a disposable copy.
```

### Catalog reviewer prompt

```text
Review the catalog at <commit or snapshot> against the NumPy/PyTorch
fluency goal in docs/CONTENT_DESIGN.md. Follow Review the catalog in
docs/DRILL_AUTHORING.md and use docs/README.md for document ownership.

Inventory the stated scope by primary outcome and overlapping families.
Trace actual assessed skills, prerequisite capabilities, discovery metadata
and plausible learning routes. Look beyond the existing map and milestones
for meaningful gaps. Explain which apparent duplicates earn separate practice.

Report concrete assessment defects, curriculum recommendations and optional
improvements separately, with locations, evidence and learning consequences.
State the inspected scope, executed probes and limits. Keep the candidate
read-only and preserve review evidence for later decisions or rechecks.
```
