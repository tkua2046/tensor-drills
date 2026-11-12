# Aggregate feature means by group rubric

## Ground truth

Repeated destinations contribute all observations; sums divide by each group's own count. Ignored -1 is not a wrapped index.

## Assessment

Unsorted repeated IDs, absent groups and ignored/empty observations assess grouped accumulation and denominator safety. Inspect the native accumulation rather than a loop over groups.

Fixed cases: `group means 0`, `group means 1`, `group means 2`, `group means 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
