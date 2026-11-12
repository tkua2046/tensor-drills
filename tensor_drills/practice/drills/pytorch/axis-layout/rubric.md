# Move sequence axes without losing the batch rubric

## Ground truth

A permutation changes which axis a coordinate names; reshaping alone does not exchange those coordinates. Only the declared singleton axis is removed and then inserted.

## Assessment

Singleton cases expose indiscriminate squeeze, and distinct lengths/values expose reshape used as permutation. Inspect the native removal, permutation and insertion operations; accept equivalent slicing of the named unit axis.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
