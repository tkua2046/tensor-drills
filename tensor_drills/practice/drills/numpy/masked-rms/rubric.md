# Normalize allowed entries by their RMS rubric

## Ground truth

Only valid entries contribute to the squared sum and denominator. A zero-norm branch produces zeros without invalid arithmetic.

## Assessment

Signed and unequal-count rows distinguish mean square from mean or a time denominator. Empty/zero-norm cases require exact zeros; inspect safe native reduction/division.

Fixed cases: `RMS 0`, `RMS 1`, `RMS 2`, `RMS 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
