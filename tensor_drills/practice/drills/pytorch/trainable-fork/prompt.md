# Create an independent trainable fork

PyTorch · Atomic create

**Goal.** Create an independent trainable leaf from a tensor with existing history.

Implement `trainable_fork(source)` in [attempt.py](attempt.py).

- `source` is a nonempty 1D CPU float64 tensor requiring gradients, with finite values in `[-3,3]`. It may be a leaf, a nonleaf, or a noncontiguous view.
- Return an independent trainable leaf with the same values, shape and dtype, requires_grad=True and no grad_fn. Leave source values and history unchanged.
- Backpropagating a new objective through the fork must populate only the fork's gradient, without reaching source or its upstream leaf. Mutating the fork under no_grad must leave source unchanged.

A copied tensor may still have history; a detached tensor may still share data. The fork must satisfy both independence properties.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/trainable-fork
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
