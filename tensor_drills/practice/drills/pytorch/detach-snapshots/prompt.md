# Separate gradient history from storage sharing

PyTorch · Atomic create

**Goal.** Produce detached tensors with the same values and different storage relationships to a trainable source.

Implement `detach_snapshots(source)` in [attempt.py](attempt.py).

- `source` is a nonempty 1D CPU float64 tensor with `requires_grad=True`. It may be a leaf, a nonleaf with history, or a noncontiguous positive-stride view. Values are finite in `[-3,3]`.
- Return `(shared, independent)`, both detached with the same values, shape and dtype as source. Neither output has gradient history or requires gradients.
- Creating the outputs must leave source values and gradient history unchanged. Later writes through shared must reach source, while independent must remain unchanged. Later writes through independent must not change source.

Detaching a value and making a copy are separate storage and gradient-tracking decisions.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/detach-snapshots
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
