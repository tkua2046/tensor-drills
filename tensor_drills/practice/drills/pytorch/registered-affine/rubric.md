# Register parameter, persistent and temporary state rubric

## Ground truth

Parameters participate in optimization; both buffers follow module conversions; only persistent buffers join checkpoints.

## Assessment

Names, initialization, actual forward and scale gradients distinguish registration from plain attributes. Different source/destination state and scratch values assess checkpoint persistence. Inspect real parameter/buffer registration. The checker snapshots injected center/scratch values and requires exact preservation after forward and backward, independently of persistence checks.

Fixed cases: `registered state 3`, `registered state 1`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
