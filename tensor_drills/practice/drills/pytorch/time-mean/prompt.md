# Average each sequence over time

PyTorch · Atomic create

**Goal.** Average over time to reduce `(batch, time, features)` to `(batch, features)`.

Implement `time_mean(values)` in [attempt.py](attempt.py).

- `values` is a CPU PyTorch tensor of shape `(B,T,F)`, with `B >= 0`, `F >= 0`, and `1 <= T <= 32`. Dtype is float32 or float64. Entries are finite and between `-100` and `100`; input may be noncontiguous and does not require gradients.
- Return shape `(B,F)`, with each feature averaged over time separately for its sequence, and the input dtype. Keep both surviving axes, including singleton and zero dimensions. Leave the input unchanged.
- Use vectorized PyTorch reductions rather than Python loops over batches, timesteps, or features.

Floating error is allowed separately for each output: `factor * (abs(expected_mean) + mean(abs(contributing values)))`, with factor `1e-5` for float32 and `1e-12` for float64.

For `[[[1], [2], [9]], [[4], [8], [15]]]`, return `[[4], [9]]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/time-mean
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Explain the reduction axis, surviving shape, and averaging denominator in your implementation.
