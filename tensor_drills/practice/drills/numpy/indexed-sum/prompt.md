# Sum contributions at indexed destinations

NumPy · Atomic create

**Goal.** Sum values into indexed destinations, adding all contributions at repeated indices.

Implement `indexed_sum(values, destinations, size)` in [attempt.py](attempt.py). Each input value contributes to the output position given by its destination index.

- `values` is a one-dimensional NumPy array of length `N`, with dtype `int32`, `int64`, `float32`, or `float64`. `0 <= N <= 100`; values are finite and between `-100` and `100`.
- `destinations` is an `int64` array of shape `(N,)`. `size` is a nonnegative Python integer, and every destination is in `[0, size)`. If `size` is zero, both inputs are empty.
- Return a array of shape `(size,)` with the same dtype as `values`. Output position `j` contains the sum of **all** contributions whose destination is `j`; unused positions are zero. Empty input still returns `size` zeros.
- Leave both inputs unchanged. Use vectorized NumPy operations rather than a Python loop over contributions.

Floating sums allow accumulation-order differences. At each destination, the error allowance is `factor * (abs(expected_sum) + sum(abs(contributions)))`, with `factor = 1e-5` for float32 and `1e-12` for float64. The contribution magnitude is computed separately for each destination. Integer sums and unused output zeros are exact.

For `values = [3, 5, 7]`, `destinations = [1, 1, 3]`, and `size = 5`, return `[0, 8, 0, 7, 0]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/indexed-sum
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the accumulation operation you used and explain how it handles repeated destinations.
