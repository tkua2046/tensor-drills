# Build and invert a Boolean mask

PyTorch · Atomic create

**Goal.** Construct a Boolean mask from two bounds and return its complement.

Implement `build_masks(values, lower, upper)` in [attempt.py](attempt.py). Mark values inside the supplied interval, then return the mask for values outside it as well.

All tensors in this drill are on CPU.

- `values` is a PyTorch tensor with at least one dimension and dtype `int64`, `float32`, or `float64`. All values and bounds are between `-100` and `100` inclusive.
- `lower` and `upper` are Python numbers that are exactly representable as `float32`, such as `0` or `0.5`. They satisfy `lower <= upper`. Bounds may be fractional even when `values` contains integers.
- Return `(inside, outside)` as a tuple of Boolean tensors, both with the same shape as `values`.
- Inside means at least `lower` and strictly below `upper`. Outside is the logical complement of inside. Leave `values` unchanged.

For `values = [-2, 0, 3, 4]`, `lower = 0`, and `upper = 4`, the masks are `[False, True, True, False]` and `[True, False, False, True]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run this command from the drill workspace root.

```sh
tensor-drills check pytorch/build-mask
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Include a sentence explaining which mask contains each endpoint and why.
