# Use true-class denominators for accuracy rubric

## Ground truth

Count correct predictions within each true class, dividing by that true class's observed count. Ignored labels contribute nothing.

## Assessment

Unequal frequencies and predictions concentrated in a different class separate true/predicted denominators and global accuracy. Inspect native grouped correctness/count accumulation.

Fixed cases: `class accuracy 0`, `class accuracy 1`, `class accuracy 2`, `class accuracy 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
