# Debug training with inline validation

PyTorch · Composite debug

**Goal.** Diagnose incorrect behavior when validation runs between training updates, then verify the repair across batches.

This trainer evaluates the same validation set after each optimizer update. The first validation result looks right. Later training updates disagree with the expected weights. Repair [attempt.py](attempt.py).

Repair `train_with_validation(model, optimizer, batches, validation_features)`. Use the supplied model and optimizer.

- For every `(features, labels)` pair, perform one forward pass in training mode and one optimizer update from that batch's mean cross-entropy loss.
- After each update, perform one forward pass on `validation_features` in evaluation mode with gradient recording disabled.
- Return a list or tuple containing one validation logits tensor per update, in batch order.

For example, with batches A and B, the calls should produce an update for A, validation logits for that state, an update for B, and validation logits for the new state.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run this command from the drill workspace root. Expect the untouched starter to fail on later updates.

```sh
tensor-drills check pytorch/inline-validation
```

For review, save your code and check output. Explain each cause of incorrect behavior and how you verified the repair.
