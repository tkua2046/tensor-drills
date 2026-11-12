# Accumulate and clear leaf gradients

PyTorch · Atomic create

**Goal.** Observe gradient accumulation across fresh forwards and clear it before a new objective.

Implement `gradient_sequence(x)` in [attempt.py](attempt.py).

- `x` is a nonempty 1D CPU float64 trainable leaf, with `x.grad is None` initially. Values are finite in `[-3,3]`.
- Backward through `sum(x*x)` and save its gradient. Make a fresh forward for `sum(3*x)`, backward without clearing, and save the accumulated gradient.
- Clear the gradient, then make a fresh forward and backward through `sum(x**3)`. Return `(first, accumulated, cleared)` as detached independent gradient snapshots. Leave the final third gradient in `x.grad`.
- Clearing to None or zero is allowed. Do not change x's data or tracking state. Snapshots must remain unchanged when the leaf's gradient or another snapshot is later mutated.

For `x=[-2,0,1]`, snapshots are `[-4,0,2]`, `[-1,3,5]`, and `[12,0,3]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/gradient-sequence
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
