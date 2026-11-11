# Classifier repair rubric

## Ground truth

1. **Gradients carry over between training batches.** The starter calls `loss.backward()` without clearing the gradient buffers. The first update starts with empty buffers. On the next call, backpropagation adds the current batch's gradients to the previous batch's gradients. Each update should use only the gradient of the supplied batch's mean cross-entropy loss.
2. **Evaluation can run in training mode.** The starter uses `torch.no_grad()`, which disables gradient recording. It leaves the model's mode untouched, so dropout remains active if the model is in training mode, including after a training call. Evaluation should use the model's inference behavior, return repeatable logits for the same inputs and parameters, and leave parameters unchanged.

## Assessment

| Intended bug | Evidence from the checks | What the learner should explain |
| --- | --- | --- |
| Gradients carry over | `two training updates` uses distinct batches with dropout disabled and compares weights and biases after each optimizer step. The starter's first update agrees with the reference and its second update diverges. Both should agree after repair. | Why the first update can look correct, how the gradient from the first batch affects the second update, and what their fix does about it. |
| Evaluation can run in training mode | `repeated evaluation` runs the same inputs twice with a model that contains dropout. It checks inference mode and disabled gradient recording on both forwards, reference logits, and unchanged parameters. | Why disabling gradient recording leaves the model's mode untouched and how their fix gives repeatable evaluation. |

`training after evaluation` checks the mode transition. The evaluation forward must run in inference mode, and the next training forward must run in training mode with gradients enabled and produce the expected update.

Accept the named check output or equivalent evidence from the learner. Read their explanation alongside the code to confirm that they identified both causes. [Fixed cases](tests.json)
