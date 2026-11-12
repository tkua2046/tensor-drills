# Repair accumulation that loses a small residual rubric

## Ground truth

The starter reduces using a float32 accumulator and casts the already-rounded total. Small contributions can disappear before conversion. Promoting before or during reduction preserves every quarter-unit contribution within the stated envelope.

## Assessment

- `lost unit residual`, `negative residual`, and `multiple contributions` expose summing in float32 and casting afterward. Ordinary, singleton and empty cases check scalar shape and dtype.
- Ask the learner to identify when precision is lost and the actual accumulator or equivalent accurate method. Accept promoted NumPy reduction or compensated approaches that meet the exact contract.
- An accurate formula alone is insufficient diagnosis: connect the repair to the starter's order of reduction and conversion.

[Fixed cases](tests.json)
