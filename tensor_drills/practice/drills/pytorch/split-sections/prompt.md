# Split unequal sections and rejoin them

PyTorch · Atomic create

**Goal.** Split an array or tensor into unequal sections along a supplied axis and rejoin them in order.

Implement `split_sections(values, sizes, axis)` in [attempt.py](attempt.py).

- `values` is a two-dimensional tensor with dtype `int64`, `float32`, or `float64`. Floating values are finite. Either dimension may be zero. It may be noncontiguous.
- `axis` is 0 or 1. `sizes` is a nonempty Python list of nonnegative integers whose sum equals `values.shape[axis]`.
- Return `(parts, restored)`. `parts` is a list or tuple with one tensor per size, in order. Each part retains both axes and the input dtype, including zero-width or zero-height parts. `restored` joins those parts in order and equals the input in shape, dtype, and values.
- Leave `values` unchanged. Parts and reconstruction may share storage; this drill does not require independent copies.
- Use PyTorch sectioning and joining operations. Bookkeeping over section sizes is allowed; Python loops over array or tensor elements are not.
- All tensors are on CPU and inputs do not require gradients. Autograd is outside this drill.

For `[[1, 2, 3], [4, 5, 6]]`, `axis=1`, and `sizes=[2, 0, 1]`, the parts have shapes `(2, 2)`, `(2, 0)`, and `(2, 1)`; rejoining gives the original matrix.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/split-sections
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the sectioning and joining operations. Explain how the size list determines the boundaries used by your implementation.
