# Convert values to a requested dtype rubric

## Ground truth

The result has the requested dtype, exactly the input shape, and values from native casting of the stored input. Float-to-integer conversion truncates toward zero. An unchanged dtype may return the same object; independence is not required.

## Assessment

`truncate toward zero` exposes rounding or flooring. `widen stored float` confirms that widening retains the stored float32 value. `same dtype`, `empty axes`, and `strided input` cover permitted aliasing, shape, and layout. Inspect the actual casting/conversion operation; accept equivalent native conversions and explain the source and requested dtypes.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)
