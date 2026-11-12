# Search event boundaries

NumPy · Composite create

**Goal.** Locate insertion boundaries and count sorted events in half-open intervals.

Implement `sorted_events(events, queries, lower, upper)` in [attempt.py](attempt.py).

Inputs are ascending int64 events `(N,)`, query points `(Q,)`, and lower/upper vectors `(R,)` with lower<=upper. N,Q,R are 0–64. Return left and right insertion indices for every query and the count of events in each half-open interval [lower,upper). Preserve query order; duplicates count separately. Use native boundary search rather than per-query scans. All int64 values, including extremes, are allowed.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/sorted-events
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
