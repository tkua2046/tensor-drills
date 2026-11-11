# Tensor Drills development notes

Start with the [documentation index](docs/README.md) when editing or reviewing project docs. It explains where each kind of decision belongs.

## Checks and builds

From the project directory, run `python -m unittest discover -s tests` to test the CLI and workspace handling. Run `uv build` to build a wheel and source distribution. See the [README](README.md) for Python requirements and installation.

For the template, verification steps, and reviewer handoff, use the [drill authoring guide](docs/DRILL_AUTHORING.md).
