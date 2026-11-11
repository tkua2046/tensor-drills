# NumPy and PyTorch Interview Drill Design

Tensor Drills provides NumPy and PyTorch exercises for hands-on ML coding interviews. Each drill pairs a small Python task with local tests and a review rubric.

## Goals and non-goals

### Goals

- Help learners practice individual tensor skills and apply them in realistic create and debug tasks.
- Make every drill independently runnable and assessable from its supplied materials.
- Help learners find prerequisite practice and choose what to work on next.
- Provide repeatable local checks and rubrics a person or an LLM can use.
- Let authors add exercises through the documented drill format.

### Non-goals

- Full mock interview orchestration
- Multi-stage exercise orchestration, including tracking progress, unlocking later tasks, and carrying submissions between stages
- Overall interview readiness scoring
- Hosted grading

## Using a drill

### Learner workflow

1. **Choose a drill.** Use `tensor-drills list` to choose NumPy or PyTorch, then narrow the choices by topic, scope (atomic or composite), and task type (create or debug). Check the goal and prerequisites to see whether the drill fits. Use its workload rating and the prompt's expected submission to gauge how much work it asks for. [Example catalog entries](#example-catalog-entries)
2. **Do the drill.** Read the prompt and write or repair the code in the starter. In a debug drill, reproduce the failure and identify its cause. Run the fixed tests as you work and save your final code, test output, and any explanation the prompt requests.
3. **Test and grade the attempt.** Use the fixed test results to check behavior. The learner or a reviewer applies the rubric to criteria that require judgment, citing evidence from the code, test output, or explanation.

Use the feedback to decide what to practice next. If the attempt exposed a gap, a linked prerequisite drill may help.

### Optional follow-ups

- During a session, a human or LLM reviewer can ask a reasoning question or request a small code change based on the learner's attempt. For example, ask why a second training batch can expose gradient carryover. If an explanation is required for the main attempt, request it in `prompt.md` and describe what counts as evidence in `rubric.md`.
- For reusable coding practice, use a standalone drill with its own goal, prompt, starter, fixed tests, and rubric. It can revisit a skill in a different context or add a requirement. Include any working code the new task builds on in its starter. For example, inline validation revisits classifier debugging in a loop that runs validation after each update. [Inline validation drill](../tensor_drills/examples/drills/pytorch/inline-validation/prompt.md)

When a follow-up drill assumes a skill taught by the earlier drill, point to the earlier drill using [`practice_drill`](#linking-prerequisites) in the follow-up's prerequisites. For related practice with no prerequisite, link the follow-up at the end of the earlier prompt as optional next practice.

### Optional LLM roles

For an interview-style attempt, an LLM can present the task, clarify the requirements, and ask follow-up questions. The learner does the coding, diagnosis, and explanation.

The learner can also ask an LLM to recommend a drill from the available catalog entries based on a practice goal and prior knowledge, or to review a completed attempt using the prompt, rubric, and submission.

## Drill model

### Scope and task type

**Atomic** drills isolate one mechanism. **Composite** drills ask the learner to combine several mechanisms to complete a recognizable ML task.

**Create** drills start from a stub. **Debug** drills start from faulty code and ask the learner to reproduce the failure, explain the cause, and verify a fix.

| Scope | Create | Debug |
| --- | --- | --- |
| **Atomic** | **NumPy** · Gather one score per row using column indices.<br>**PyTorch** · Compute a shared bias gradient from batched upstream gradients. | **NumPy** · Fix the axis in a row-wise mean.<br>**PyTorch** · Fix a parameter snapshot that changes during training. |
| **Composite** | **NumPy** · Implement batched masked attention with stable softmax and fully masked rows.<br>**PyTorch** · Implement a token classification update that excludes padding from the loss. | **NumPy** · Fix the selection axis and label alignment in batched nearest neighbor search.<br>**PyTorch** · Fix gradient accumulation across batches and active dropout during evaluation. |

### Catalog metadata

Each cataloged drill stores its metadata in `metadata.json` beside the prompt. The drill directory supplies the ID and library. Use the schema when authoring metadata. The `list` command checks the fields it uses and tolerates extra fields and repeated topics in existing workspaces. [Metadata schema](drill-metadata.schema.json)

- **Library** identifies NumPy or PyTorch using the first part of the drill ID, such as `numpy` in `numpy/row-gather`.
- **Scope** identifies an atomic or composite drill.
- **Task type** identifies a create or debug drill.
- **Goal** describes one observable outcome the learner will practice and demonstrate. Write one sentence in the prompt, tie it to a fixed test or rubric item, and use the same sentence in the metadata.
- **Topics** are a list of labels for discovery. A drill can have several, such as `indexing`, `shapes`, and `dtypes`. Reuse preferred labels across drills.
- **Prerequisites** lists the capabilities the drill assumes. Give each item a short, freeform `capability` statement and an optional `practice_drill` ID for an existing drill that teaches or practices it. Use `[]` when there are no prerequisites.
- **Workload** rates the amount of work in the main attempt on a 1–5 scale. Assume the learner meets the prerequisites. Consider how much code they need to read, write, or debug and what they need to verify or explain.

Use these anchors for workload. Assign 2 or 4 to drills that fall between them. Drills that ask for a similar amount of work can share a rating.

| Rating | Typical task |
| --- | --- |
| 1 | One small function or fix with straightforward verification. |
| 3 | Several related behaviors to implement or diagnose and verify. |
| 5 | A larger task with several interacting components and substantial verification. |

### Example catalog entries

| Field | [numpy/row-gather](../tensor_drills/examples/drills/numpy/row-gather/prompt.md) | [pytorch/classifier](../tensor_drills/examples/drills/pytorch/classifier/prompt.md) |
| --- | --- | --- |
| Library | NumPy | PyTorch |
| Scope | Atomic | Composite |
| Task type | Create | Debug |
| Goal | Gather one score per row using its supplied column index and verify the result's shape and dtype. | Diagnose incorrect behavior across training and evaluation, then verify the repair across multiple batches. |
| Topics | `indexing`, `shapes`, `dtypes` | `training-loop`, `autograd`, `evaluation` |
| Prerequisites | Read a 2D array's shape and index an element. | Follow the forward pass, loss, backward pass, and optimizer step in a basic training loop. |
| Workload | 1 | 3 |

- For NumPy practice with `indexing` and `shapes`, choose row gathering if you know basic 2D indexing and want an atomic create drill. Its workload is 1 because you implement one function and explain how rows pair with columns.
- For PyTorch practice with `training-loop` and `evaluation`, choose classifier debugging if you can follow a basic training loop and want a composite debug drill. Its workload is 3 because you reproduce and repair failures in two functions and explain how you verified the fixes across batches.

### Linking prerequisites

Inline validation assumes the learner can reason about state across training and evaluation calls. Its metadata points to classifier debugging for practice with that prerequisite. [Inline validation metadata](../tensor_drills/examples/drills/pytorch/inline-validation/metadata.json)

```json
{
  "capability": "Follow a PyTorch training step and an evaluation pass, and explain how their state can affect the next call.",
  "practice_drill": "pytorch/classifier"
}
```

`tensor-drills list` shows the practice drill ID under the prerequisite. It also shows `Prepares for: pytorch/inline-validation` on the classifier entry, using the same metadata. Filters narrow the displayed entries while the relationship comes from the workspace catalog. Learners who already meet the prerequisite can start directly.

## Drill package and assessment

### Files and setup

In a practice workspace, each drill lives in `drills/<library>/<name>/` and has an ID such as `numpy/row-gather`. The package supplies what the learner needs to start and check the task, including any working code it builds on.

- **`prompt.md`** is the task brief the learner reads before attempting the drill.
- **`metadata.json`** describes the drill for catalog discovery.
- **`attempt.py`** holds the editable stub or faulty starter.
- **Fixed tests** use `tests.json` to record inputs and expected results and `verify.py` to check each case against the attempt.
- **`rubric.md`** records the intended diagnosis or behavior and the evidence a reviewer uses to assess an attempt.

### Learner prompt

The learner should be able to start, run, and submit the drill using `prompt.md` and its links.

- **Task.** State the goal and what to implement or repair. Link the editable starter. For a debug drill, describe the observable failure.
- **Contract.** State the interface, input assumptions, required behavior, and any constraints that affect whether an attempt is valid. For debug drills, describe what a correct run does and let the learner infer which state or API calls to change. Use a short example when it clarifies the expected behavior.
- **Run and submit.** Link the shared setup and name the drill's dependencies. Give the check command, working directory, expected result from the untouched starter, and what to submit. For debug drills, ask for the updated code, check output, and a brief explanation of the cause and verification.

Put the intended diagnosis and repair guidance in `rubric.md` for review after the attempt. Keep full test cases in `tests.json` and discovery fields such as topics and workload in `metadata.json`. The shared README covers environment setup. [Workspace README](../tensor_drills/examples/README.md)

### Fixed tests

From a workspace created with `tensor-drills init`, run `tensor-drills check <drill-id>`. The checker runs the current `attempt.py` in a fresh Python process and compares its outputs or resulting state with the expected results in the manifest. It reports each case and uses distinct exit statuses for a pass, a candidate failure, and a setup error.

Use fixed tests for correctness and add larger inputs where they can reliably expose violations of a stated efficiency requirement.

When authoring cases, calculate expected results by hand or with a reference run and save them in the manifest. Verify that the untouched starter fails as described in the prompt, a known-good answer passes, and a plausible wrong answer fails. For a debug drill with multiple bugs covered by fixed tests, leave each bug in place while fixing the others and check that a case still fails.

### Reviewer rubric

Use `rubric.md` after the attempt. It gives a human or LLM reviewer the context to assess the submission alongside the prompt and check output. Include two sections.

- **Ground truth.** For a debug drill, list every intended bug. For each one, state what triggers it, its cause, and the behavior a correct repair restores. For a create drill, describe the behavior and edge cases a correct implementation handles.
- **Assessment.** State what counts as evidence in the code, check output, or learner's explanation. Refer to automated cases by name and identify any regression checks that cover interactions or behavior beyond an individual bug. Accept equivalent evidence and repairs that meet the contract.

Use the learner prompt as the source for graded requirements. Keep fixture inputs and expected results in `tests.json`. General code quality suggestions are advisory.

## Pilot

The pilot uses NumPy row gathering and PyTorch classifier debugging to see whether learners can start a drill, run the checks, and use the feedback. Inline validation shows how a second PyTorch drill can build on classifier debugging.

### NumPy atomic create

Implement `gather_scores(scores, columns)`. Given scores of shape `(N, C)` and valid integer column indices of shape `(N,)`, return the selected values in row order with shape `(N,)` and the input score dtype. For example, `[[10, 20, 30], [40, 50, 60]]` with columns `[2, 0]` gives `[30, 40]`.

Use a rectangular input to expose axis mistakes and repeated column indices to check that each row contributes a value. Use one-row and one-column inputs to check the same contract with singleton dimensions. [Row gathering drill](../tensor_drills/examples/drills/numpy/row-gather/prompt.md)

### PyTorch composite debug

Repair a small CPU classifier with dropout, an optimizer, and two labeled batches. The starter carries gradients between batches and evaluates with dropout active. Each training call must enter training mode and apply one update using the current batch's cross-entropy gradient. Evaluation must return logits in evaluation mode without recording gradients.

Start with fixed weights and a fixed random state. Check the weights after each update and check repeated evaluation. Use training after evaluation as a regression check for the mode transition. The rubric lists the two intended bugs and the evidence for each repair. [Classifier debugging drill](../tensor_drills/examples/drills/pytorch/classifier/prompt.md) · [Reviewer rubric](../tensor_drills/examples/drills/pytorch/classifier/rubric.md)

### Validation and rollout

1. **Validate the exercises.** Validate the fixed tests for each drill and check that a second valid implementation also passes. [Fixed test validation](#fixed-tests)
2. **Try the pilot with a learner.** Review the classifier attempt with the rubric. If the learner tries inline validation, check whether they can diagnose and verify a related bug in the new code. Record time to first run, requirements that needed clarification, and gaps in the tests or rubric. Use those observations to revise the drill format.
3. **Expand the catalog.** Fill the remaining cells in both banks using the examples in the drill model. Add further drills where learners show a recurring gap or a fresh task can check transfer.
