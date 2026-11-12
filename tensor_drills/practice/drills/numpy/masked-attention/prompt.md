# Compose masked scaled attention

NumPy · Composite create

**Goal.** Combine scaled query-key scores, safe masked normalization and value weighting.

Implement `masked_attention(q, k, v, mask)` in [attempt.py](attempt.py).

Float64 q `(B,Q,D)`, k `(B,K,D)`, v `(B,K,E)` have magnitude at most4, B,D,E=1–4 and Q,K=0–4. Boolean allowed mask has rank three with singleton or matching `(B,Q,K)` axes. Return float64 `(B,Q,E)`: softmax of q@k.T/sqrt(D) over allowed keys, weighted by v. Fully excluded or no-key queries return exact zero. Preserve float64 throughout normalization. No gradients are involved.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-attention
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
