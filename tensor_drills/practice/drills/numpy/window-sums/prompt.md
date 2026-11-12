# Build shared windows and sum snapshots

NumPy · Composite create

**Goal.** Return overlapping shared windows and their moving-sum snapshots.

Implement `window_sums(x, width)` in [attempt.py](attempt.py).

Input is a writable int64 vector of length 1–64, magnitude at most one million, and width in [1,N]. Return read-only shared overlapping windows `(N-width+1,width)` at step one, plus an independent int64 moving-sum snapshot `(N-width+1,)`. Construction must preserve source values and writability. Later source writes must reach every overlapping occurrence while the sums remain unchanged. Empty input and invalid widths are outside the contract.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/window-sums
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
