# Maintain stable streaming entropy

NumPy · Composite create

**Goal.** Maintain softmax entropy with fixed-size state independent of chunk boundaries.

Implement `entropy_state(); entropy_update(state, chunk); entropy_value(state)` in [attempt.py](attempt.py).

Implement the three functions in the starter. State is an immutable tuple of at most four numeric scalars, with no retained arrays/history in state, globals or closures; its scalar magnitudes are unrestricted. Each update returns a valid state and preserves its inputs. Float64 chunks contain finite logits in [-1000,1000], length 0–64, total stream length at most one million. Return softmax entropy in nats as a Python float or float64 scalar; empty streams return exact zero. Results must be independent of chunk boundaries. Callers may iterate chunks; updates may not loop over values. Save reasoning about retained state and temporary storage.

Use native vectorized operations. Preserve input data, shapes and dtypes. Independent dimensions are 1–8 unless another bound is stated; derived extents follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/streaming-entropy
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
