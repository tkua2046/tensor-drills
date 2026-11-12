# Compute aligned-token global cross-entropy rubric

## Ground truth

The denominator counts valid tokens globally. Ignored entries contribute neither loss nor gradients; the zero case retains a source graph.

## Assessment

Unequal valid counts and extreme confidently wrong targets distinguish denominator and probability-underflow mistakes. Compare independent loss/gradients and exact ignored zeros. Accept native summed cross-entropy or stable log-softmax plus gathering.

Fixed cases: `token loss 0`, `token loss 1`, `token loss 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
