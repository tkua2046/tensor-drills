# Deduplicate rows with reconstruction

NumPy · Atomic create

**Goal.** Deduplicate rows and reconstruct original row order through inverse indices.

Implement `unique_rows(x)` in [attempt.py](attempt.py).

Supply int64 `(N,F)`, with N=0–8 and F=1–8. Return lexicographically sorted unique rows `(K,F)` and native-integer inverse indices `(N,)`, such that unique[inverse] reconstructs x. Deduplicate whole rows, not individual elements.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/unique-rows
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
