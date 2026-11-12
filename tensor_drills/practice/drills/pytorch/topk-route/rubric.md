# Route selected feature vectors to destinations rubric

## Ground truth

One selected index order aligns scores, features and destinations; accumulated totals and their gradients stay within each batch item.

## Assessment

Different rankings and repeated/unused destinations expose selection and accumulation errors. Nonuniform upstream totals check selected source gradients and exact unused zeros. Inspect native gather/accumulation.

Fixed cases: `feature routing 0`, `feature routing 1`, `feature routing 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
