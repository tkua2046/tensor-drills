# Compare paired and Cartesian indexing

NumPy · Atomic create

**Goal.** Use the same indices to select coordinate pairs and every row and column combination.

Implement `select_entries(matrix, rows, columns)` in [attempt.py](attempt.py). Use NumPy array indexing with the supplied index arrays to form both selections.

- `matrix` is a 2D NumPy array with dtype `int32`, `int64`, `float32`, or `float64`. `rows` and `columns` are integer index arrays of the same shape `(K,)`, with `K >= 1`. Indices are nonnegative and in bounds. They may be unsorted or repeated.
- Return `(paired, grid)`. In the `(K,)` result `paired`, entry `i` comes from coordinate `(rows[i], columns[i])`.
- In the `(K, K)` result `grid`, entry `(i, j)` comes from coordinate `(rows[i], columns[j])`. Preserve the order and repeats in both index lists.
- Both results are arrays with the matrix dtype. Leave all inputs unchanged.

For `matrix = [[10, 20, 30], [40, 50, 60]]`, `rows = [1, 0]`, and `columns = [0, 2]`, the paired result is `[40, 30]` and the grid is `[[40, 60], [10, 30]]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/paired-cartesian
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Briefly describe the indexing operations and index shapes your code uses, and how they produce the two result shapes.
