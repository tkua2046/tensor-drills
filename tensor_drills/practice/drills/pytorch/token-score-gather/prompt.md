# Gather scores at batch/time target indices

PyTorch · Atomic create

**Goal.** Gather each token's target-class score while preserving its gradient path.

Implement `token_score_gather(x, targets)` in [attempt.py](attempt.py).

Supply a trainable float64 leaf `(B,T,C)`, initially with no gradient, and valid int64 targets `(B,T)`. Return `(B,T)` containing `x[b,t,targets[b,t]]`, connected to the supplied source. Preserve its tracking state and empty gradient buffer during the call. Values have magnitude at most16; inputs may be noncontiguous.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/token-score-gather
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
