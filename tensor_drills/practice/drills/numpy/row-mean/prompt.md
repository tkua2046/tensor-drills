# Repair one mean per row

NumPy · Atomic debug

**Goal.** Return one mean per row of a 2D array.

A helper promises one mean per row, but returns the wrong shape or values. Repair `row_mean(values)` in [attempt.py](attempt.py).

- `values` is a two-dimensional NumPy array of shape `(R,C)`, with `R >= 0` and `1 <= C <= 32`. Dtype is float32 or float64. Entries are finite and between `-100` and `100`; input may be noncontiguous.
- Return shape `(R,)`, with one mean over each row's columns and the input dtype. Preserve the row dimension, including one row or zero rows. Leave the input unchanged.
- Use vectorized NumPy reductions rather than Python element loops.

Floating error is allowed separately for each output: `factor * (abs(expected_mean) + mean(abs(contributing values)))`, with factor `1e-5` for float32 and `1e-12` for float64.

For `[[1, 2, 6], [3, 8, 10]]`, return `[3, 7]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/row-mean
```

The untouched starter fails the row-axis and shape checks. For review, save your code and check output. Explain the reduction axis, surviving shape, and averaging denominator in your implementation.
