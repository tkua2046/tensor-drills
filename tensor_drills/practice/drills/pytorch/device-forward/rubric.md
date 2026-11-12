# Place a model, inputs and new offsets together rubric

## Ground truth

Model state, placed inputs and newly allocated offsets share the target device and dtype. Adding offsets creates model input without modifying the caller, even when a CPU transfer returns the same object.

## Assessment

- CPU and available-device cases inspect parameters, registered buffer, returned input and offsets. Only the device explicitly printed was exercised.
- On CPU-only setups inspect code for device propagation and hard-coded CPU allocations, which values alone cannot distinguish. Accept creating then moving offsets or direct allocation on the target; discuss extra copies where useful.

[Fixed cases](tests.json)
