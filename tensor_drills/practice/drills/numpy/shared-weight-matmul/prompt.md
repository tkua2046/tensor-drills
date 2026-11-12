# Multiply batches by one shared weight matrix

NumPy · Atomic create

**Goal.** Multiply each batch item of shape `(rows, in_features)` by the same `(in_features, out_features)` matrix.

Implement `shared_weight_matmul(values, weights)` in [attempt.py](attempt.py).

- `values` has shape `(B, R, I)` and `weights` has shape `(I, O)`. Dimensions are positive, with `1 <= I <= 32`.
- Both inputs have matching dtype, either float32 or float64. Entries are finite and between `-100` and `100`. Inputs may be noncontiguous.
- Return shape `(B, R, O)` and the input dtype, satisfying `result[b, r, o] = sum_i values[b, r, i] * weights[i, o]`. The same weights apply to every batch item.
- Leave both inputs unchanged. Use vectorized NumPy contraction operations without Python loops over batches, rows, or features.
- Floating error is allowed separately for each output: `factor * (abs(expected) + sum(abs(contributing products)))`, with factor `1e-5` for float32 and `1e-12` for float64. Add `I * smallest_subnormal(dtype)` to this allowance for underflow rounding, where `smallest_subnormal` is the smallest positive representable value of that dtype.

For `values=[[[1, 2]], [[3, 4]]]` and `weights=[[1, 0, 2], [0, 1, 3]]`, return `[[[1, 2, 8]], [[3, 4, 18]]]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/shared-weight-matmul
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the contraction operation and axis. Explain how the shared weights apply to different batch items and how the output axes are determined.
