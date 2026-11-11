# Tensor Drills development notes

## Checks and builds

From the project directory, run `python -m unittest discover -s tests` to test the CLI and workspace handling. Run `uv build` to build a wheel and source distribution. See the [README](README.md) for Python requirements and installation.

## Author a drill

For a custom drill, create `drills/<library>/<name>/` in a practice workspace. For a bundled drill, use `tensor_drills/examples/drills/<library>/<name>/` in the project. Add the prompt, starter, test manifest, verifier, and review rubric. Each case in `tests.json` has a unique `name`, `inputs`, and `expected` results. List required import names in `dependencies`.

Use `prompt.md` to give learners the task, its contract, and the steps to run and submit it. [Learner prompt guidance](docs/DESIGN.md#learner-prompt)

Use `rubric.md` to record the intended behavior or bugs and the evidence for assessing a submission. [Reviewer rubric guidance](docs/DESIGN.md#reviewer-rubric)

For a catalog entry, add `metadata.json` beside the prompt. Use the same goal sentence in both files. When you include a `practice_drill` link, check that the ID resolves to a drill that teaches or practices the prerequisite. [Metadata schema](docs/drill-metadata.schema.json) · [Workload anchors and examples](docs/DESIGN.md#catalog-metadata)

In `verify.py`, define `check_case(call, inputs, expected)`. Construct fresh inputs from the case, use `call("function_name", ...)` to invoke learner functions, and raise an assertion with an explanation when the result differs from the expected behavior. Keep expected results in the manifest. Run the starter, a correct attempt, and plausible incorrect attempts before sharing a drill. [Fixed test validation](docs/DESIGN.md#fixed-tests)

Package reusable coding follow-ups as standalone drills. Supply the code and checks needed to start from a fresh workspace. Use `practice_drill` to link earlier prerequisite practice, or a prompt link for other related practice. [Follow-up guidance](docs/DESIGN.md#optional-follow-ups)
