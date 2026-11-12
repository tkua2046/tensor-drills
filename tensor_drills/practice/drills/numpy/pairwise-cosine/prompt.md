# Compute signed pairwise cosine similarity

NumPy · Composite create

**Goal.** Compute pairwise cosine similarities with exact zeros for zero-vector pairs.

Implement `pairwise_cosine(x, y)` in [attempt.py](attempt.py).

Float64 collections x `(M,D)` and y `(N,D)` have M,N=0–8, D=1–8. Each coordinate is zero or has magnitude in [1e-6,16]. Return `(M,N)` signed cosine similarity. Every pair involving a zero vector is exact zero. Do not add epsilon to nonzero norms.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/pairwise-cosine
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
