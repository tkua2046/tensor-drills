# Assign through a mask so aliases see the update

PyTorch · Atomic create

**Goal.** Replace selected entries in place so existing aliases observe the change.

Implement `masked_assign(values, mask, replacement)` in [attempt.py](attempt.py).

- `values` has one to three dimensions, possibly with empty axes, and dtype `int32`, `int64`, `float32`, or `float64`. Floating values are finite. The input may itself be a noncontiguous basic-slice view into a larger tensor.
- `mask` is a Boolean tensor with exactly the shape of `values`. `replacement` is a finite Python number exactly representable in the value dtype; for integer values it is an integer.
- Replace entries selected by true mask positions in place. Leave all other entries, shape, and dtype unchanged, and leave the mask unchanged. Existing aliases and views of the input must observe the edit. If the input is a view into a larger tensor, only its selected positions may change in that source.
- Return `None`. Use PyTorch assignment or equivalent native mutation operations rather than Python element loops.
- All tensors are on CPU and inputs do not require gradients. Autograd is outside this drill.

For `values=[[1, 2], [3, 4]]`, `mask=[[True, False], [False, True]]`, and `replacement=-7`, the same input becomes `[[-7, 2], [3, -7]]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/masked-assign
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Identify the operation that mutates the existing storage, and explain why rebinding a local variable or editing an advanced-index temporary would not satisfy the contract.
