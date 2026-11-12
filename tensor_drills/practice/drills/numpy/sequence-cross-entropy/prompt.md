# Average token loss within each valid prefix

NumPy · Composite create

**Goal.** Compute each sequence's mean cross-entropy over its valid prefix.

Implement `sequence_cross_entropy(x, targets, lengths)` in [attempt.py](attempt.py).

Float64 logits are `(B,T,C)` in [-1000,1000], int64 targets `(B,T)` and lengths `(B,)` in [0,T], with `0<=T<=8`. Valid-prefix targets are class IDs; padding may contain -100. Return `(B,)` mean cross-entropy over each sequence's own valid prefix. Empty prefixes return exact zero. Compute stable log normalization; this is not a single global token mean.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/sequence-cross-entropy
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
