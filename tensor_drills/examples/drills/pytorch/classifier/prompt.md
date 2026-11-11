# Repair a classifier's training and evaluation

PyTorch · Composite debug

**Goal.** Diagnose incorrect behavior across training and evaluation, then verify the repair across multiple batches.

A classifier's first training update looks correct, but the next batch leaves the parameters in the wrong state. Evaluation can also give different logits for the same input and weights. Reproduce the failures and repair [attempt.py](attempt.py).

- `train_step(model, optimizer, features, labels)` runs the model for training and applies one optimizer update from the supplied batch's mean cross-entropy loss. This must work across consecutive training calls and after evaluation.
- `evaluate(model, features)` runs the model for inference and returns logits without recording gradients or changing parameters. With the same inputs and unchanged parameters, repeated calls should return the same logits, including immediately after training.
- Use the supplied model and optimizer. Each call makes one forward pass. The checker uses CPU tensors, with features shaped `(N, D)` and integer class labels shaped `(N,)`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run this command from the drill workspace root.

```sh
tensor-drills check pytorch/classifier
```

Expect the untouched starter to fail behavioral checks. For review, save the updated code and check output. Explain the cause of each failure and how you verified the repair.
