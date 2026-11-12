# Build broadcastable prefix key validity

PyTorch · Atomic create

**Goal.** Construct a broadcastable key-validity mask from each sequence's length.

Implement `key_length_mask(lengths, keys)` in [attempt.py](attempt.py).

Int64 lengths `(B,)` lie in [0,keys], with `0<=keys<=8`. Return Boolean `(B,1,1,keys)` whose entry is true exactly when key position is less than that sequence's length. Keep the batch axis for B=1 and handle keys=0. Use a broadcast comparison without materializing head/query repetitions.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/key-length-mask
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
