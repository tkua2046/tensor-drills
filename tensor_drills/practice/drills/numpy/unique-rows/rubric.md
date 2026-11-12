# Deduplicate rows with reconstruction rubric

## Ground truth

Inverse indices map each original row to a sorted unique row; they differ from first-occurrence indices.

## Assessment

Correctness: separated duplicates, unsorted/negative rows, singleton features and no observations. Inspect native row uniqueness and explain inverse reconstruction.

Fixed cases: `unique reconstruction 0`, `unique reconstruction 1`, `unique reconstruction 2`, `unique reconstruction 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
