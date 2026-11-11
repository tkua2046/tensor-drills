# Independent slice repair rubric

## Ground truth

The starter's basic slice shares storage with `values`. Its in-place addition therefore changes the source before returning. A repair must obtain independent data before an edit that could reach the source, or construct an independent edited result without mutating that source. Copying after editing the view leaves the initial source mutation unfixed.

The returned tensor contains the selected entries plus the increment, with the selected shape and source dtype. Source and result stay independent under later writes, including when the increment is zero. Empty slices retain shape `(0,)`. Arithmetic uses the source dtype, including scalar conversion before addition. In `scalar rounding before addition`, the increment rounds to `-1000` in float32, so the edited value is zero; higher-precision scalar arithmetic is not the contract.

## Assessment

- **Correctness and mutation.** `middle slice` exposes the source change during the call. `stepped slice` checks selection order and a non-unit step. `zero increment still independent` separates equal values from independent storage. For each nonempty result, the verifier writes to the result and then to the source and checks that changes do not cross over. Singleton and empty cases check shape preservation.
- **Diagnosis and operations.** Ask the learner to identify the actual basic slice and the operation that creates independent data in their repair. Their explanation should connect shared storage to the starter's mutation, and explain why copying after the edit is insufficient. Accept copying the source before slicing, copying the slice before editing, or constructing a new edited result with equivalent PyTorch operations.
- **Efficiency and clarity.** The prompt requires PyTorch slicing and tensor operations rather than Python element loops. Inspect the actual operations in the repair. Discuss unnecessary full-source copies when only a small slice is needed, without rejecting a correct repair solely for that choice.
- **Storage reasoning.** `detach()` changes gradient tracking, not storage ownership. `contiguous()` may return the same storage for an already contiguous slice. Require mutation evidence rather than pointer comparisons alone.

[Fixed cases](tests.json)
