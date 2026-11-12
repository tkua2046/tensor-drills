# Accumulate int32 readings without overflow

NumPy · Atomic create

**Goal.** Sum int32 readings exactly in an int64 accumulator.

Implement `safe_integer_sum(values)` in [attempt.py](attempt.py).

- `values` is a one-dimensional int32 NumPy array with at most 64 entries. Every int32 value is permitted; all possible totals fit int64.
- Return the exact total as a `numpy.int64` scalar, including zero for empty input. Leave the input unchanged.
- Use NumPy operations rather than Python element loops. Equivalent native integer promotion is allowed.

For `[2147483647, 1]`, return `numpy.int64(2147483648)`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/safe-integer-sum
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Explain the actual operations and numeric or RNG choices in your implementation.
