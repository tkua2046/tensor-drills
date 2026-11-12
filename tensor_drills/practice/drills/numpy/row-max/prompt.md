# Keep row maxima aligned with indices

NumPy · Atomic create

**Goal.** Return each row's maximum together with its first matching column index.

Implement `row_max(x)` in [attempt.py](attempt.py).

Input int64 data is `(R,C)` with R possibly zero and C positive. Return `(maxima, indices)`, each shaped `(R,)`. Maxima retain the value dtype; indices use a native integer dtype. For tied maxima, choose the first column in that row. Inputs may be noncontiguous.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/row-max
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
