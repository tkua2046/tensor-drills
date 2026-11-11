# Gather one score per row

NumPy · Atomic create

**Goal.** Gather one score per row using its supplied column index and verify the result's shape and dtype.

Implement `gather_scores(scores, columns)` in [attempt.py](attempt.py). Each row of `scores` contains the scores for one item. The corresponding entry in `columns` identifies the score to return for that row.

- `scores` is a NumPy array of shape `(N, C)`, with `N >= 0` and `C >= 1`.
- `columns` is a NumPy integer array of shape `(N,)`. All indices are in `[0, C)`.
- Return a NumPy array of shape `(N,)` with the same dtype as `scores`, in row order. Leave both inputs unchanged.

For `scores = [[10, 20, 30], [40, 50, 60]]` and `columns = [2, 0]`, the result is `[30, 40]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/row-gather
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Include a sentence explaining how each row gets its own column index.
