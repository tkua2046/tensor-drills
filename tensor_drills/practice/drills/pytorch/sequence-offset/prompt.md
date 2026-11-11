# Repair per-sequence offsets

PyTorch · Atomic debug

**Goal.** Apply each sequence's `(batch, features)` offset at every time step of a `(batch, time, features)` tensor.

A helper adds each sequence's feature offsets to its timesteps. For some input shapes it raises a dimension error; for others it returns the expected shape with wrong values. Repair `add_sequence_offsets(values, offsets)` in [attempt.py](attempt.py).

- `values` has shape `(B, T, F)` and `offsets` has shape `(B, F)`, with positive integer dimensions. Both are CPU PyTorch tensors with matching dtype, either `float32` or `float64`. Inputs are finite, between `-100` and `100`, and do not require gradients.
- Return a tensor of shape `(B, T, F)` and the input dtype, satisfying `result[b, t, f] = values[b, t, f] + offsets[b, f]`.
- Leave both inputs unchanged. Use PyTorch broadcasting without Python loops over batches, timesteps, or features, and without storing repeated copies of the offsets. Floating results are checked with relative and absolute tolerances of `1e-6`.

For two sequences with two timesteps and one feature, `values = [[[1], [2]], [[3], [4]]]` and `offsets = [[10], [100]]` should give `[[[11], [12]], [[103], [104]]]`.

If needed, consult the official [broadcasting rules](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#general-semantics) for a general shape reference.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run this command from the drill workspace root.

```sh
tensor-drills check pytorch/sequence-offset
```

The untouched starter fails the unequal-length case with a dimension error and the equal-length case with incorrect values. For review, save your code and check output. Identify the operand shapes in your repair. Explain why the starter can return the right shape while assigning offsets to the wrong positions.
