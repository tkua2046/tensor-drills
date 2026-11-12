# Solve while preserving RHS rank

NumPy · Atomic create

**Goal.** Solve a supplied linear system while preserving vector or matrix right-hand-side rank.

Implement `solve_system(a, rhs)` in [attempt.py](attempt.py).

Supply float64 SPD coefficients `(D,D)`, D=1–4, eigenvalues in [1,65] and coefficient magnitude at most 65. RHS is `(D,)` or `(D,K)` of magnitude at most16, K=1–8. Return the same RHS shape solving a@solution=rhs. Use a native solver or factorization/solves; do not construct an explicit inverse. Singular handling and batched coefficients are outside this task.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/solve-system
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
