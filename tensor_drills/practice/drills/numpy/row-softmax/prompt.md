# Normalize each row with stable softmax

NumPy · Atomic create

**Goal.** Normalize each row of logits into stable probabilities.

Implement `row_softmax(values)` in [attempt.py](attempt.py).

- `values` is a 2D NumPy array of shape `(R,C)`, with `R >= 0`, `1 <= C <= 32`, and dtype float32 or float64. Logits are finite and between `-10000` and `10000`.
- Return the same shape and dtype. For each row, probability `j` is `exp(values[j]) / sum(exp(values))` evaluated stably for that row. Leave the input unchanged. Empty rows retain shape `(0,C)`.
- Use elementary NumPy operations, without Python loops over rows or elements, or a third-party softmax helper. Outputs must be finite; negligible exponential underflow to zero is allowed.
- Checks use relative tolerance `1e-5` for float32 or `1e-12` for float64, plus an absolute allowance of twice the dtype's smallest positive subnormal value.

Each row `[1000, 1000, 1000]` has probabilities `[1/3, 1/3, 1/3]` despite the large common offset.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/row-softmax
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Explain the actual operations and numeric or RNG choices in your implementation.
