# Draw reproducible row indices with a local generator rubric

## Ground truth

Fresh caller-seeded PCG64 choice defines each draw and its order. Global legacy seeding, module-level state carried between calls, sorted draws, or ignored seeds do not meet the contract.

## Assessment

- The two named seeds distinguish seed propagation. Full, singleton and empty draws preserve shape, dtype and order. Each fixed case repeats its seed after an intervening different seed.
- The verifier compares the complete legacy RNG state before and after every call, including empty draws, then restores its own probe state.
- Inspect local generator construction and use of the caller's seed. Accept equivalent constructors and index-population representations with the declared choice semantics; a different sampling algorithm is outside this reproducibility contract.

[Fixed cases](tests.json)
