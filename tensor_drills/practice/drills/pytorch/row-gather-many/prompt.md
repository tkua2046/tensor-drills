# Gather several columns independently per row

PyTorch · Atomic create

**Goal.** Gather several columns independently for each row, preserving selection order and repeats.

Implement `gather_columns(values, columns)` in [attempt.py](attempt.py).

- `values` is a matrix of shape `(N, C)`, with `N >= 0`, `C >= 1`, and dtype `int32`, `int64`, `float32`, or `float64`. It may be noncontiguous; floating values are finite.
- `columns` is an int64 tensor of shape `(N, K)`, with `K >= 0`. All indices are in `[0, C)`.
- Return shape `(N, K)` and the input value dtype, satisfying `result[i, j] = values[i, columns[i, j]]`. Preserve each row's selection order and repeats, including when either output dimension is zero.
- Leave both inputs unchanged. Use vectorized PyTorch indexing or gathering operations rather than Python element loops.
- All tensors are on CPU and inputs do not require gradients. Autograd is outside this drill.

For `values=[[10, 20, 30], [40, 50, 60]]` and `columns=[[2, 0, 2], [1, 1, 0]]`, return `[[30, 10, 30], [50, 50, 40]]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/row-gather-many
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the indexing or gathering operations and the shapes that keep each selection paired with its own row.
