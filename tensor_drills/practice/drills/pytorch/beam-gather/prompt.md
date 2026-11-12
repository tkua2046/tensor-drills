# Select beam parents on the middle axis

PyTorch · Atomic create

**Goal.** Select beam features along the middle axis while preserving batch identity and repeated-parent gradients.

Implement `beam_gather(x, parents)` in [attempt.py](attempt.py).

Trainable float64 leaf features are `(B,K,F)` with no incoming gradient. Parent indices are valid int64 `(B,W)` with `0<=W<=8`. Return `(B,W,F)` with `out[b,w,f]=x[b,parents[b,w],f]`. Preserve source state during the call. Repeated parents accumulate gradients; empty selection must remain connected and yield a zero source gradient. Use native selection without materialized repeated feature indices.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/beam-gather
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
