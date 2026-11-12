# Compose attention with absolute causality

PyTorch · Composite create

**Goal.** Compute rectangular causal attention with absolute positions and finite Q/K/V gradients.

Implement `causal_attention(q, k, v, qpos, kpos, qvalid, kvalid)` in [attempt.py](attempt.py).

Trainable float64 q `(B,H,Q,D)`, k `(B,H,K,D)` and v `(B,H,K,E)` have magnitude at most4. B,H,D,E=1–4; Q,K=0–6. Source gradients start None. Absolute int64 query/key positions are `(Q,)`/`(K,)`, possibly shifted or unordered; Boolean validity is `(B,Q)`/`(B,K)`. Attend only where key_position<=query_position and both flags are true. Use scaled dot products with 1/sqrt(D), no dropout. Return `(B,H,Q,E)` with exact zeros for fully excluded or no-key queries, connected to all three inputs even for empty axes. Preserve data/tracking and leave source gradients empty during forward. First-order Q/K/V gradients under arbitrary upstream weights must be finite and correct.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/causal-attention
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
