# Repair pairwise squared distances

NumPy · Composite debug

**Goal.** Repair pairwise squared distances between two collections while avoiding a `(left_rows, right_rows, features)` temporary.

Repair `pairwise_squared_distance(x, y)` in [attempt.py](attempt.py).

Float64 left and right collections are `(M,D)` and `(N,D)`, with values of magnitude at most16; M or N may be zero. Return finite nonnegative `(M,N)` squared distances. Small cancellation negatives may be clamped to zero. Do not allocate a `(M,N,D)` pair-by-feature difference array. The faulty starter can produce shape errors or incorrect distances. Explain its cause and the temporary array shapes in your repair.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/pairwise-squared-distance
```

The faulty starter fails some cases with incorrect values or a shape error. Explain the cause and the evidence for your repair. Save your code, check output and explanation for review.
