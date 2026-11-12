# Normalize each row with stable softmax

PyTorch · Atomic create

**Goal.** Normalize each row of logits into stable probabilities.

Implement `row_softmax(values)` in [attempt.py](attempt.py).

- `values` is a 2D CPU float32/64 tensor of shape `(R,C)`, `R>=0`, `1<=C<=32`, with finite logits in `[-10000,10000]`. Inputs do not require gradients.
- Return the same shape/dtype, with stable softmax probabilities normalized independently per row. Leave input unchanged. Negligible underflowed tails may be zero; outputs must be finite.
- Use vectorized PyTorch operations without Python loops over rows or elements. Native softmax or equivalent stable elementary operations are allowed.
- Checks use relative tolerance 1e-5 for float32 or 1e-12 for float64, plus an absolute allowance of twice the dtype's smallest positive subnormal value.

A row [1000,1000,1000] has uniform probabilities regardless of its large common offset.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/row-softmax
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
