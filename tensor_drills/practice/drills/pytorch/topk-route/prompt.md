# Route selected feature vectors to destinations

PyTorch · Composite create

**Goal.** Select the highest-scoring items in each batch and sum their feature vectors at the associated destinations.

Implement `topk_route(scores, x, dest, groups, k)` in [attempt.py](attempt.py).

Nontrainable float64 scores `(B,N)` are distinct per row. Trainable float64 leaf features are `(B,N,F)` with no incoming gradient; int64 destinations are `(B,N)` in [0,groups). Select `0<=k<=N` highest scores per batch in descending order. Return indices `(B,k)` and summed selected features `(B,groups,F)`. Repeated destinations accumulate; unused groups are exact zero. Keep totals connected to x even for k=0 and preserve source tracking/gradient state during the call.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/topk-route
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
