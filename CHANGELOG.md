# Changelog

## Unreleased

### Added

- Add core practice in both tracks with dtype conversion, unequal splits, per-row multiple gathering, replacement, masked assignment, shared-weight matrix products, and single-axis means.
- Practice independent slice repair and repeated-index accumulation in both tracks, plus PyTorch per-sequence broadcasting repair.
- Practice Boolean masks, stacking and concatenation, paired and Cartesian indexing, and multi-axis reductions in both NumPy and PyTorch.
- Start PyTorch practice with an atomic row-gathering drill.
- Try an optional array and tensor indexing warm-up from the practice workspace.

## 0.1.0 - 2026-11-11

### Added

- Create editable practice workspaces and run fixed checks through the `tensor-drills` CLI or the Python API.
- Practice NumPy row gathering, PyTorch classifier debugging, and PyTorch inline validation with fixed checks and Markdown review rubrics.
- Author custom drills with JSON test manifests and Python verifiers.
- Bundle catalog metadata for the example drills and document its JSON schema.
- List and filter drills by library, scope, task type, topics, and workload with `tensor-drills list`.
- Show which drills a prerequisite practice drill prepares learners for.
