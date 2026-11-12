# Select a subset with partition

NumPy · Atomic create

**Goal.** Select the largest k values and their original indices using partition selection.

Implement `partition_topk(x, k)` in [attempt.py](attempt.py).

Supply distinct int64 values `(N,)`, N=0–64, and k=0–N. Return selected values and original indices, both `(k,)`, for the largest k values. Output order is unrestricted; each index must stay paired with its value. Use native partition selection when 0<k<N. Do not use a full sort to choose the subset.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/partition-topk
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
