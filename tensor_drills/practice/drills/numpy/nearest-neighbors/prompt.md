# Find nearest rows in bounded reference blocks

NumPy · Composite create

**Goal.** Find each query's nearest reference row using bounded distance blocks and a deterministic tie rule.

Implement `nearest_neighbors(x, y, block)` in [attempt.py](attempt.py).

Float64 queries are `(M,D)` with `0<=M<=32`; references `(N,D)` have `1<=N<=256`. Coordinates are integer-valued in [-16,16]. Block size is1–64. Return native-integer indices and float64 squared distances, both `(M,)`; ties choose the smallest global reference index. A reference-block loop, 2D query-by-block distance tiles and running best arrays are allowed. Do not allocate a full query-by-reference distance matrix when N exceeds block, or pair-by-feature differences. Save allocation-shape reasoning with your solution.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded. A loop over reference blocks is allowed.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/nearest-neighbors
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
