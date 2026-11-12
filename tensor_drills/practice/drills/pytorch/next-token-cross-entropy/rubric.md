# Compute next-token global cross-entropy rubric

## Ground truth

The denominator counts valid shifted pairs globally. Ignored entries contribute neither loss nor gradients; the zero case retains a source graph.

## Assessment

Unequal valid counts and extreme confidently wrong targets distinguish denominator and probability-underflow mistakes. Compare independent loss/gradients and exact ignored zeros. Short sequences and unused final logits assess temporal alignment.

Fixed cases: `next-token 0`, `next-token 1`, `next-token 2`, `next-token 3`, `next-token 4`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
