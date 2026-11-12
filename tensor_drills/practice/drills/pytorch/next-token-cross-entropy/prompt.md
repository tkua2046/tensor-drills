# Compute next-token global cross-entropy

PyTorch · Composite create

**Goal.** Compute global valid-token cross-entropy after aligning each logit with the next token.

Implement `next_token_cross_entropy(x, targets)` in [attempt.py](attempt.py).

Trainable float64 leaf logits are `(B,T,C)` in [-1000,1000] with no incoming gradient. Int64 targets are `(B,T)`, containing valid classes or -100. T may be zero or one. Pair logits at t with targets at t+1; final-position logits are unused. Return one scalar mean over all valid next-token pairs across the entire batch. Empty/all-ignored results are exact zero and remain connected to all logits, giving zero gradients. Use raw logits with stable log normalization. Preserve caller data, tracking and gradient buffers during the call.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/next-token-cross-entropy
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
