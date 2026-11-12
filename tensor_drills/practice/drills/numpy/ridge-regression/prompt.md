# Fit an unaveraged ridge objective

NumPy · Composite create

**Goal.** Fit ridge coefficients for an explicitly unaveraged regularized least-squares objective.

Implement `ridge_regression(x, targets, lam)` in [attempt.py](attempt.py).

Float64 x is `(N,F)` of magnitude at most2, targets `(N,)` or `(N,K)` of magnitude at most16; N=0–8, F=1–4, K=1–8, lam in [0.25,4]. Minimize sum((x@W-targets)**2)+lam*sum(W**2), without intercept or averaging by N. Return `(F,)` or `(F,K)` matching target rank. No observations means exact zero coefficients.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/ridge-regression
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
