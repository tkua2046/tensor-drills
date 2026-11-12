# Standardize selected observations rubric

## Ground truth

Filter first, then calculate per-feature population statistics. Identical stored values are a constant feature even when a floating std calculation reports tiny noise.

## Assessment

Excluded outliers expose statistics over all rows; population/sample distinctions and singleton/constant cases expose unsafe scaling. Inspect native selection and constant detection.

Fixed cases: `standardize 0`, `standardize 1`, `standardize 2`, `standardize 3`, `standardize 4`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
