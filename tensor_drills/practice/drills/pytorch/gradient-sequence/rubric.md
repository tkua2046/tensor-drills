# Accumulate and clear leaf gradients rubric

## Ground truth

Backward adds to existing gradient buffers. The second gradient is 2*x+3; clearing makes the third contain only 3*x². Stored snapshots need their own data.

## Assessment

- The cases distinguish clearing too early, not clearing before the third objective, and returning live gradient-buffer aliases.
- Inspect the three actual backward calls, their fresh forwards, and snapshot construction. Analytic assignments alone miss the operation requirement. Accept grad=None or zeroing.

[Fixed cases](tests.json)
