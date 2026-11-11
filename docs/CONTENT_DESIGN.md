# Content Design

## Purpose and scope

Tensor Drills helps learners who know basic Python become fluent in NumPy and PyTorch. Fluency means being able to choose an operation, predict its shape and effects, and implement or debug it on a fresh input. Each library has its own practice path. Learners can start with either one and choose exercises based on the skills they need. Each shipped exercise includes its instructions, starter, fixtures, tests, and rubric in Tensor Drills.

The curriculum covers everyday array and tensor operations, their use in numerical and training tasks, and selected deeper topics. The [infrastructure design](INFRA_DESIGN.md) owns how an exercise is packaged and assessed.

## How we choose drills

- **Plan coverage by learning outcome.** Use the skill map to identify the skills each track should cover. For each proposed drill, record the skill it teaches, the gap it fills, and the evidence that would show the learner met the goal. Use the delivery plan to schedule the drills. Record the public references that informed the curriculum and each exercise. [Resources and drill sources](RESOURCES.md)
- **Prioritize by learning value.** Start with operations that recur across tasks or cause common errors. Follow them with practical compositions and then topics that benefit from prior fluency. A useful outcome keeps its place in the map even when its available exercise needs better checks or later delivery.
- **Choose one default exercise per outcome per library.** When candidates cover the same outcome, keep the stronger exercise. Use useful cases from the other candidate to strengthen its checks or offer a repeat with different inputs or context. Give an exercise its own outcome when it asks the learner to reason about something new, such as a different reduction denominator, mutation that must reach aliases, or a backward requirement.
- **Match the task to the goal.** Use an atomic drill to isolate a mechanism, a composite drill to practice combining operations, and a debug drill when a realistic mistake has an observable symptom. Count only the outcomes the tests or rubric assess. For example, checking a gathered result does not cover constructing a Boolean mask or aligning Cartesian indices. [Scope and task type](INFRA_DESIGN.md#scope-and-task-type) · [Assessment](INFRA_DESIGN.md#drill-package-and-assessment)

## Learning paths

Each track starts with core operations and builds toward applied tasks and topics for deeper practice. Learners can practice the shared skills in their chosen library and return to an isolated operation when an applied task exposes a gap. [Shared skills](SKILL_MAP.md#shared-skills)

### NumPy path

Apply the shared array operations to numerical calculations and data processing. [NumPy skills and drills](SKILL_MAP.md#numpy)

### PyTorch path

Build on the shared tensor operations with autograd, model training, and model state. [PyTorch skills and drills](SKILL_MAP.md#pytorch)

## Delivery model

Each library follows its own milestone sequence and ships drills as they meet the acceptance criteria. Use a common authoring brief when the learning outcome matches. Each drill includes its own starter, fixtures, checks, and rubric. [Content implementation plan](CONTENT_IMPLEMENTATION_PLAN.md)
