# Gather scores with ignored target IDs rubric

## Ground truth

Sentinel equality takes precedence over index validity. A valid-column sentinel is still ignored; an unindexable sentinel cannot be gathered before masking.

## Assessment

Ignore=0 and -100 cases distinguish sentinel precedence and safe gathering. Check real native indexing and an explanation of the safe index domain.

Fixed cases: `ignored gather 0`, `ignored gather 1`, `ignored gather 2`, `ignored gather 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
