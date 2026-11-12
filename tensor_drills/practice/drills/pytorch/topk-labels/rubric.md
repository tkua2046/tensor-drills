# Keep top-k scores and labels aligned rubric

## Ground truth

The same selected index order drives score and label gathering. Only selected scores receive upstream gradients.

## Assessment

Per-batch rankings and unrelated labels expose misalignment; negative scores and k=0 assess boundaries. Accept top-k or sorting plus native gathers.

Fixed cases: `ranked labels 0`, `ranked labels 1`, `ranked labels 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
