# Reduce across axes and center the input

NumPy · Composite create

**Goal.** Reduce across multiple axes, keep dimensions for broadcasting, and use the result to center the input.

Implement `reduce_and_center(values)` in [attempt.py](attempt.py). For each position on the middle axis, use NumPy reductions to summarize all values at that position. Use broadcasting to subtract their mean.

- `values` is a NumPy array of shape `(B, R, C)` with positive dimensions and dtype `float32` or `float64`. The values are finite and have magnitude at most 100.
- Return `(totals, means, centered)`. Sum over axes 0 and 2 for `totals` of shape `(R,)`. Average over those same axes for `means` of shape `(1, R, 1)`.
- Subtract each middle-axis position's mean from every corresponding input value. The `centered` result has shape `(B, R, C)`.
- All outputs are arrays with the input dtype. Leave `values` unchanged. The checks compare floating-point values with relative and absolute tolerances of `1e-6`.

For two batches of two rows and two columns, `values = [[[1, 3], [2, 6]], [[5, 7], [10, 14]]]`. The totals are `[16, 32]`, the means are `[[[4], [8]]]`, and the centered result is `[[[-3, -1], [-6, -2]], [[1, 3], [2, 6]]]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/reduce-axes
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Briefly describe the reduction operations and axes your code uses, and how the operand shapes in the subtraction broadcast.
