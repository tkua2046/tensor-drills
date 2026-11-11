# Repair an independently editable slice

NumPy · Atomic debug

**Goal.** Edit a slice and return it with storage independent of the source.

A helper returns the right edited values, but callers find that the source changes too. Repair `edit_slice(values, start, stop, step, increment)` in [attempt.py](attempt.py).

- `values` is a one-dimensional NumPy array, with dtype `int64`, `float32`, or `float64`. Values and `increment` are finite and between `-1000` and `1000`. For integer input, `increment` is an integer. Arithmetic uses the input dtype: convert the scalar increment to that dtype before adding it.
- `start`, `stop`, and `step` are Python integers satisfying `0 <= start <= stop <= len(values)` and `step >= 1`. Empty inputs and empty slices are allowed.
- Return the entries selected by `values[start:stop:step]`, in order, with `increment` added to each. Preserve the selected shape and input dtype. Floating results are checked with relative and absolute tolerances of `1e-6`.
- Leave `values` unchanged throughout the operation. The returned array must be writable and independent: later mutations of either the source or the result must not change the other.

Use NumPy slicing and array operations rather than Python element loops to construct the result.

For `[10, 20, 30, 40]`, `start=1`, `stop=3`, `step=1`, and `increment=100`, return `[120, 130]` while the source stays `[10, 20, 30, 40]`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/independent-slice
```

The untouched starter fails source-preservation and independence checks for nonempty slices. For review, save your code and check output. Explain why the starter changes the source and how your repair prevents changes in either direction. Identify the slicing and storage-related operations in your code.
