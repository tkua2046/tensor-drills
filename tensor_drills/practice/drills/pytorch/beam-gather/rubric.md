# Select beam parents on the middle axis rubric

## Ground truth

Each batch has its own parent order. Repeated parent selections add their upstream feature gradients.

## Assessment

Per-batch ordering, repeated parents, singleton features and no selected beams assess layout and backward behavior. Inspect native index alignment and zero-stride expansion instead of repeat.

Fixed cases: `beam features 0`, `beam features 1`, `beam features 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
