import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tensor_drills import init_workspace


ROOT = Path(__file__).resolve().parents[1]


class ListTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        self.workspace = init_workspace(self.root / "practice")

    def run_list(self, *args, workspace=None):
        return subprocess.run(
            [
                sys.executable, "-m", "tensor_drills.cli", "list",
                "--workspace", str(workspace or self.workspace), *args,
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=15,
        )

    def test_lists_metadata_in_drill_id_order_and_skips_unlisted_drills(self):
        legacy = self.workspace / "drills/numpy/legacy"
        legacy.mkdir()
        (legacy / "prompt.md").write_text("An older drill.\n", encoding="utf-8")

        result = self.run_list()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(
            result.stdout.index("numpy/row-gather"), result.stdout.index("pytorch/classifier")
        )
        self.assertIn("Gather one score per row", result.stdout)
        self.assertIn("Read a 2D array's shape", result.stdout)
        self.assertIn("\npytorch/inline-validation (composite debug", result.stdout)
        self.assertIn("Prepares for: pytorch/inline-validation", result.stdout)
        self.assertIn("(practice: pytorch/classifier)", result.stdout)
        self.assertNotIn("numpy/legacy", result.stdout)

    def test_filters_by_each_catalog_field(self):
        for option, value, expected, excluded in (
            ("--library", "pytorch", "pytorch/classifier", "numpy/row-gather"),
            ("--scope", "atomic", "numpy/row-gather", "pytorch/classifier"),
            ("--task-type", "debug", "pytorch/classifier", "numpy/row-gather"),
            ("--topic", "indexing", "numpy/row-gather", "pytorch/classifier"),
            ("--workload", "3", "pytorch/classifier", "numpy/row-gather"),
        ):
            with self.subTest(option=option):
                result = self.run_list(option, value)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(expected, result.stdout)
                self.assertNotIn(excluded, result.stdout)

    def test_requires_every_topic_and_combines_filters(self):
        result = self.run_list("--library", "numpy", "--topic", "indexing", "--topic", "shapes")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("numpy/row-gather", result.stdout)

        for filters in (
            ("--topic", "indexing", "--topic", "autograd"),
            ("--library", "numpy", "--task-type", "debug"),
        ):
            with self.subTest(filters=filters):
                result = self.run_list(*filters)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("No drills match", result.stdout)
                self.assertNotIn("numpy/row-gather", result.stdout)
                self.assertNotIn("pytorch/classifier", result.stdout)

    def test_reports_invalid_metadata_with_its_path(self):
        metadata = self.workspace / "drills/pytorch/classifier/metadata.json"
        broken = json.loads(metadata.read_text(encoding="utf-8"))
        broken["topics"] = "autograd"
        for contents, detail in (("{", "JSON"), (json.dumps(broken), "topics")):
            with self.subTest(detail=detail):
                metadata.write_text(contents, encoding="utf-8")
                result = self.run_list()
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("pytorch/classifier/metadata.json", result.stderr)
                self.assertIn(detail, result.stderr)

        result = self.run_list("--library", "numpy")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("numpy/row-gather", result.stdout)

    def test_prepares_for_uses_prerequisites_even_when_dependent_drill_is_filtered_out(self):
        path = self.workspace / "drills/pytorch/classifier/metadata.json"
        metadata = json.loads(path.read_text(encoding="utf-8"))
        metadata["prerequisites"].extend([
            {"capability": "Pair rows with column indices.", "practice_drill": "numpy/row-gather"},
            {"capability": "Select one score per row.", "practice_drill": "numpy/row-gather"},
        ])
        path.write_text(json.dumps(metadata), encoding="utf-8")

        result = self.run_list("--library", "numpy")
        self.assertEqual(result.returncode, 0, result.stderr)
        row_gather = next(
            entry for entry in result.stdout.split("\n\n")
            if entry.startswith("numpy/row-gather (atomic create")
        )
        prepares_for = next(
            line.strip().removeprefix("Prepares for: ").split(", ")
            for line in row_gather.splitlines()
            if line.strip().startswith("Prepares for: ")
        )
        self.assertEqual(prepares_for.count("pytorch/classifier"), 1)
        self.assertIn("numpy/paired-cartesian", prepares_for)
        self.assertNotIn("pytorch/classifier (composite debug", result.stdout)

    def test_missing_workspace_reports_how_to_select_one(self):
        result = self.run_list(workspace=self.root)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("drills", result.stderr)
        self.assertIn("tensor-drills init", result.stderr)
