# Repair accumulation that loses a small residual

NumPy · Atomic debug

**Goal.** Sum readings with enough precision to preserve a small residual amid large values.

Repair `precise_sum(values)` in [attempt.py](attempt.py).

- `values` is a one-dimensional float32 NumPy array with at most 64 stored readings. Stored values are multiples of `0.25` with magnitude at most `2**28`.
- Return the exact total as a `numpy.float64` scalar, including zero for empty input. Leave the input unchanged.
- These bounds make every partial sum exactly representable in float64. Use an accumulator or equivalent calculation that preserves the small contributions; returning a widened value after an inaccurate reduction is insufficient.

For stored float32 readings `[100000000, 1, -100000000]`, return `numpy.float64(1)`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/precise-sum
```

The starter loses small contributions in the cancellation cases. For review, save your code and check output. Explain the actual operations and numeric or RNG choices in your implementation.
