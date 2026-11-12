# Normalize grouped scores and preserve presence

NumPy · Composite create

**Goal.** Normalize scores within groups while distinguishing absent groups from all-negative-infinity groups.

Implement `grouped_probabilities(scores, ids, groups)` in [attempt.py](attempt.py).

Supply scores `(N,)`, finite in [-1000,1000] or negative infinity, int64 IDs in [0,groups), and groups=1–8; N=0–32. Return maxima `(groups,)`, native-integer counts `(groups,)` and probabilities `(N,)`. Absent maxima are negative infinity/count zero. A present all-negative-infinity group has uniform probabilities over its members. Otherwise normalize finite scores stably and give negative-infinity members exact zero. NaN and positive infinity are excluded.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/grouped-probabilities
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
