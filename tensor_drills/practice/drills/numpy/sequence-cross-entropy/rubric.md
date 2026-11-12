# Average token loss within each valid prefix rubric

## Ground truth

Stable log probabilities avoid probability-underflow infinities. Each sequence has its own denominator and safe ignored-padding indices.

## Assessment

Unequal counts and extreme confidently wrong targets distinguish global averaging and probability-then-log arithmetic. Inspect native log normalization and masking.

Fixed cases: `sequence loss 0`, `sequence loss 1`, `sequence loss 2`, `sequence loss 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
