# Save state and restore a fresh model rubric

## Ground truth

The saved state includes registered parameters and persistent buffers. Loading into the provided fresh model preserves its identity and modes while giving independent state.

## Assessment

- Distinct initial destination state, a nondefault buffer and deterministic predictions verify restoration. The file is loaded independently and its keys/values checked. Later source mutation checks independence.
- Inspect actual save/load and use of that saved file. A direct in-memory copy plus a separately correct file can pass data checks but misses the file-restoration requirement.

[Fixed cases](tests.json)
