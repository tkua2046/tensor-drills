# Fit an unaveraged ridge objective rubric

## Ground truth

The regularization belongs to the stated sum objective. Averaging data error without rescaling lambda changes the optimum. Positive lambda makes rank-deficient systems well defined.

## Assessment

Correctness: rank deficiency, underdetermined data, multiple targets, different regularization and empty observations. Operations: accept regularized solve or augmented least squares. Explain the objective scaling and resulting coefficient shape.

Fixed cases: `ridge objective 0`, `ridge objective 1`, `ridge objective 2`, `ridge objective 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
