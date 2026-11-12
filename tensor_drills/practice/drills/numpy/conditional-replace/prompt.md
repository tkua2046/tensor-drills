# Replace negative values in an independent result

NumPy · Atomic create

**Goal.** Return an independent, shape-preserving result with negative entries replaced by zero.

Implement `replace_negatives(values)` in [attempt.py](attempt.py).

- `values` has one to three dimensions, possibly with empty axes, and dtype `int32`, `int64`, `float32`, or `float64`. Floating values are finite. It may be noncontiguous.
- Return an array with the input shape and dtype. Negative entries become zero; other values retain their original positions and values.
- Leave `values` unchanged. The result must be writable and independent, even when no entries need replacing. Later mutation of the input or result must not affect the other.
- Use NumPy array or tensor operations rather than Python element loops. Equivalent conditional selection, clipping, or edits on an independent copy are allowed.

For `[[-2, 0], [3, -1]]`, return `[[0, 0], [3, 0]]` and leave the original unchanged.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/conditional-replace
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the operations that preserve shape and create independent data. Explain what happens when there are no negative entries.
