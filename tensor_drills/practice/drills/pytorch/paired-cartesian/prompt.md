# Compare paired and Cartesian indexing

PyTorch · Atomic create

**Goal.** Use the same indices to select coordinate pairs and every row and column combination.

Implement `select_entries(matrix, rows, columns)` in [attempt.py](attempt.py). Use PyTorch tensor indexing with the supplied index tensors to form both selections.

All tensors in this drill are on CPU.

- `matrix` is a 2D PyTorch tensor with dtype `int32`, `int64`, `float32`, or `float64`. `rows` and `columns` are `torch.int64` index tensors of the same shape `(K,)`, with `K >= 1`. Indices are nonnegative and in bounds. They may be unsorted or repeated.
- Return `(paired, grid)`. In the `(K,)` result `paired`, entry `i` comes from coordinate `(rows[i], columns[i])`.
- In the `(K, K)` result `grid`, entry `(i, j)` comes from coordinate `(rows[i], columns[j])`. Preserve the order and repeats in both index lists.
- Both results are tensors with the matrix dtype. Leave all inputs unchanged.

For `matrix = [[10, 20, 30], [40, 50, 60]]`, `rows = [1, 0]`, and `columns = [0, 2]`, the paired result is `[40, 30]` and the grid is `[[40, 60], [10, 30]]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run this command from the drill workspace root.

```sh
tensor-drills check pytorch/paired-cartesian
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Briefly describe the indexing operations and index shapes your code uses, and how they produce the two result shapes.
