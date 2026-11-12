# Join each valid-prefix mean and last vector rubric

## Ground truth

The mean uses the valid length; last-vector indices are valid only for nonempty prefixes.

## Assessment

Different lengths and zero/one/full-length sequences assess denominator and boundary handling. Inspect native length masking, reduction and guarded gathering.

Fixed cases: `prefix summary 0`, `prefix summary 1`, `prefix summary 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
