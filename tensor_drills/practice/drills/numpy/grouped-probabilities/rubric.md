# Normalize grouped scores and preserve presence rubric

## Ground truth

An absent group and an observed all-negative-infinity group share a maximum but differ in count. Finite groups normalize after shifting; all-infinite groups require the stated uniform convention.

## Assessment

Correctness/numerics: unsorted repeated IDs, absent versus all-infinite groups, extreme finite scores and empty input. Inspect native grouped maxima and sum accumulation; exclude invalid infinity subtraction rather than suppressing warnings.

Fixed cases: `group presence 0`, `group presence 1`, `group presence 2`, `group presence 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
