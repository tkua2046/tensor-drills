# Build shared windows and sum snapshots rubric

## Ground truth

Overlapping windows repeat references to source locations. A read-only view protects against ambiguous writes through windows while preserving writes through the original source. Reductions are snapshots.

## Assessment

Storage: inspect sharing/read-only flags and observe all windows after a source mutation; test stepped and nonzero-offset sources. Correctness: width-one/full-width and interior overlap. Explain the window shape and strides; unsafe writable overlapping views are insufficient.

Fixed cases: `window ownership 0`, `window ownership 1`, `window ownership 2`, `window ownership 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
