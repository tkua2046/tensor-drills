# Compute safe masked log mass

NumPy · Composite create

**Goal.** Compute masked log-sum-exp with negative infinity for empty rows.

Implement `masked_logsumexp(x, mask)` in [attempt.py](attempt.py).

Float64 logits are `(B,T,C)` in [-1000,1000], C=0–8. Boolean mask has rank three and singleton or matching axes. Return `(B,T)` log(sum(exp(allowed logits))) over C. Empty or fully excluded rows return exact negative infinity; every nonempty row returns a finite value. No warnings, overflow, or invalid operations.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-logsumexp
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
