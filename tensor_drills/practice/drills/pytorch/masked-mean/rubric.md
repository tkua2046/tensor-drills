# Pool valid timesteps with per-sequence counts rubric

## Ground truth

Each sequence uses its own valid-timestep count, not T or the total count over the batch. A safe zero-count path prevents NaNs and warnings.

## Assessment

Unequal counts, a fully masked row, excluded finite outliers and zero timesteps expose denominator and empty-row errors. Fixed checks observe values, shape, input state and warnings, and assert exact zeros for zero-count rows. Inspect broadcast mask storage and the safe denominator in the code; value checks cannot identify materialized repeated masks.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
