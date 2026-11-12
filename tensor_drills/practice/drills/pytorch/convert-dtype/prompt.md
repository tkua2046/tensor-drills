# Convert values to a requested dtype

PyTorch · Atomic create

**Goal.** Convert numeric input to the requested dtype while preserving its shape.

Implement `convert_dtype(values, dtype)` in [attempt.py](attempt.py).

- `values` has one to three dimensions, possibly with empty axes. Supported source and requested dtypes are `int32`, `int64`, `float32`, and `float64`. Values are finite and between `-100` and `100`.
- `dtype` is a `torch.dtype` object. Return an tensor of the requested dtype with exactly the input shape. Use native casting semantics: floating values cast to integers truncate toward zero; widening a float preserves its already-stored value.
- Leave the input's values, shape, and dtype unchanged. Output independence is not required, so an unchanged-dtype result may share storage with the input.
- Use PyTorch conversion operations rather than Python element loops.
- All tensors are on CPU and inputs do not require gradients. Autograd is outside this drill.

Casting `[[-2.75, 2.75], [0, 1.9]]` to int64 gives `[[-2, 2], [0, 1]]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/convert-dtype
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the source and requested dtypes and explain the conversion operation used, including float-to-integer behavior.
