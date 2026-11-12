# Aggregate feature means by group

NumPy · Composite create

**Goal.** Compute each group's feature mean while excluding ignored observations.

Implement `group_means(x, ids, groups)` in [attempt.py](attempt.py).

Float64 observations are `(N,F)` with magnitude at most16, `0<=N<=32`, and int64 IDs `(N,)` in {-1,0,...,groups-1}. Ignore -1. Return means `(groups,F)` and native-integer counts `(groups,)`. Missing groups have exact zero means/counts. Use vectorized grouped accumulation.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/group-means
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
