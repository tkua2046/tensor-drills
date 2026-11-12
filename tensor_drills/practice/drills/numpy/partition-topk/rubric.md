# Select a subset with partition rubric

## Ground truth

A partition identifies a cutoff without globally ordering the input. Distinct inputs eliminate cutoff tie policy; k=0 needs explicit empty handling.

## Assessment

Correctness: compare the selected set and original index/value pairs, accepting arbitrary order. Operations: inspect partition selection; full sorting can pass values but misses the required skill.

Fixed cases: `partial selection 0`, `partial selection 1`, `partial selection 2`, `partial selection 3`, `partial selection 4`, `partial selection 5`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
