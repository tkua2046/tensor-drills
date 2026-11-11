# Stack and concatenate two matrices

NumPy · Atomic create

**Goal.** Combine two matrices along a new axis and along an existing axis.

Implement `join_matrices(first, second, axis)` in [attempt.py](attempt.py). Combine the matrices in two ways, using the same axis number for both.

- `first` and `second` are NumPy arrays with the same 2D shape `(R, C)`, positive dimensions, and the same dtype: `int32`, `int64`, `float32`, or `float64`. `axis` is either `0` or `1`.
- Return `(stacked, concatenated)`. In `stacked`, insert a length-two axis at `axis`: position 0 on that axis contains `first` and position 1 contains `second`. The other dimensions stay in order.
- In `concatenated`, extend the existing axis at `axis`: put all of `first` before `second` on that axis. Both outputs are arrays with the input dtype. Leave both inputs unchanged.

For `first = [[1, 2, 3]]`, `second = [[4, 5, 6]]`, and `axis = 1`, the outputs are `[[[1, 2, 3], [4, 5, 6]]]` of shape `(1, 2, 3)` and `[[1, 2, 3, 4, 5, 6]]` of shape `(1, 6)`.

Use [the Python setup](../../../README.md#setup) with NumPy. Run this command from the drill workspace root.

```sh
tensor-drills check numpy/stack-concat
```

The untouched starter reports that the function is unimplemented. For review, save your code and the check output. Include a sentence explaining how the two output shapes depend on the chosen axis.
