# Per-sequence offset repair rubric

## Ground truth

PyTorch aligns broadcast dimensions from the right. Direct addition treats the offsets' first axis as time, rather than batch. When `B != T` and both are greater than one, the starter raises a size mismatch. When `B == T`, the shapes fit but different timestep positions receive different sequences' offsets.

A repair can align offsets as `(B, 1, F)` so one sequence's offsets apply at every timestep of that sequence. Reordering the input axes so addition broadcasts across time is also valid. It preserves the input shape and dtype and leaves both inputs unchanged.

## Assessment

- **Correctness.** `unequal batch and time` exposes the dimension error. `equal batch and time` uses different offsets across sequences to expose silent misalignment despite the right output shape. `singleton time` catches accidental batch/time expansion; `singleton batch` and `singleton feature` guard dimension loss. Every case checks shape, dtype, values, and unchanged inputs.
- **Diagnosis and operations.** Ask the learner to identify the actual operands and their shapes immediately before addition. They should explain right alignment and why equal axis lengths concealed the starter's error. Accept equivalent dimension-insertion operations, including indexing, unsqueezing, reshaping, or reordering axes around the addition.
- **Efficiency.** The prompt requires broadcasting without Python element loops or stored repeated offsets. A loop or `repeat` can pass value tests but misses that requirement. Inspect the code for it; a broadcast view or `expand` does not itself store repeated copies. Check that the learner explains their chosen alignment rather than naming an API without connecting it to the axes.

[Fixed cases](tests.json)
