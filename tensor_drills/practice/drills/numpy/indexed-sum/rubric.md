# Indexed sum rubric

## Ground truth

Output `j` is the sum of every input value whose destination is `j`. Repeated indices contribute repeatedly; order does not drop earlier values. Output length comes from `size`, including unused trailing positions and empty inputs. Output dtype matches `values`, and both inputs remain unchanged.

## Assessment

- **Correctness.** `repeated destinations` distinguishes accumulation from overwriting: destination 1 receives both 3 and 5. `unsorted repeated destinations` combines repeats, negative contributions, and unused trailing output positions. `fractional contributions` and `one destination` check floating sums and prevent integer truncation.
- **Floating arithmetic.** The cancellation cases admit ordinary native accumulation-order differences under the prompt's per-destination error allowance. `many small contributions` exercises the maximum input length. `small contribution at a separate destination` ensures a large value elsewhere does not mask a missing small contribution. Unused destinations still require exact zeros.
- **Shape and dtype.** `empty input with destinations` requires four zeros without inferring length from indices. `zero output size` and `one contribution` check empty and singleton shapes. The verifier checks dtype and unchanged inputs in every case.
- **Operations.** Inspect the actual vectorized NumPy operation and the learner's explanation of repeated-index behavior. Accept `np.add.at`, weighted `np.bincount` with appropriate size and dtype handling, or another equivalent vectorized approach. Ordinary advanced-index `output[destinations] += values` is not a repeated-index reduction and loses contributions in the supplied duplicate cases.
- **Efficiency.** A Python loop can produce the right values but does not meet the stated vectorization requirement. Discuss extra allocations, such as a contribution-by-destination indicator matrix, and whether a direct indexed reduction avoids them. Equivalent valid operations remain acceptable.

[Fixed cases](tests.json)
