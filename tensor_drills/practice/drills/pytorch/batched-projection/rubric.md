# Project each sequence with its own weights rubric

## Ground truth

The mask denominator, input sequence and projection matrix remain local to each batch item. Linearity allows either order of pooling and projection.

## Assessment

Different per-item weights, unequal valid counts, rectangular features/output widths and excluded outliers expose shared-weight substitution, division by total time and cross-batch contraction. Check native contraction and mask alignment; accept equivalent calculation orders.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
