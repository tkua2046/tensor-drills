# Apply one supervised training update

PyTorch · Composite create

**Goal.** Implement one labeled training update with a supplied model, loss, and optimizer.

Implement `train_step(model, loss_fn, optimizer, features, labels)` in [attempt.py](attempt.py).

- The supplied CPU float64 classifier returns raw logits. `features` is a nonempty `(N,D)` tensor and `labels` is int64 `(N,)` with valid class indices. Inputs are finite and unchanged by the call. The supplied loss computes mean cross-entropy, and optimizer is SGD.
- Set training mode. Make exactly one model forward, one supplied loss call, and one supplied optimizer step using only the current batch gradient. Incoming gradient buffers may contain stale values, and consecutive calls use different batches.
- Return the pre-update mean loss as a detached scalar tensor. Post-step gradient buffers may be retained or cleared; at optimizer step time they must contain the current batch's gradients.

Two identical labeled examples still use their mean loss, rather than doubling the gradient.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/train-step
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
