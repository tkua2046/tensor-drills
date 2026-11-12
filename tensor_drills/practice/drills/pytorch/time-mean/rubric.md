# Average each sequence over time rubric

## Ground truth

Average over time to reduce `(batch, time, features)` to `(batch, features)`. The reduction divides the sum by the length of the named axis and preserves the input dtype and surviving axes. The input stays unchanged. Per-output error allowances admit ordinary native reduction rounding under the bounded reduction length.

## Assessment

`distinct axes` separates the time mean from a sum or middle timestep. Singleton and zero batch/feature cases preserve both output axes. The cancellation case uses a separate small feature to keep numerical allowances local to each output. Inspect the reduced axis and denominator. Accept mean or an equivalent vectorized sum/division.

Review code and explanation alongside the fixed-case output. A Python element-loop solution can pass values but misses the stated vectorization requirement.

[Fixed cases](tests.json)
