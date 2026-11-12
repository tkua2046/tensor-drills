# Compare expansion with independent repeated data rubric

## Ground truth

Broadcast expansion reuses singleton storage, while the independent result has separate element storage. NumPy read-only flags and PyTorch overlapping-write behavior differ.

## Assessment

Check zero stride and source-to-expanded propagation, then a single copied-element write. Never probe overlapping expansion writes. Inspect native expansion and copy operations, allowing equivalent ways of constructing the independent result.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
