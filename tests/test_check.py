import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CheckerTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

        self.drill = self.root / "drills" / "demo" / "double"
        self.drill.mkdir(parents=True)
        self.manifest = {
            "dependencies": [],
            "cases": [{"name": "double two", "inputs": 2, "expected": 4}],
        }
        self.write_manifest()
        (self.drill / "verify.py").write_text(
            'def check_case(call, inputs, expected):\n'
            '    assert call("double", inputs) == expected\n',
            encoding="utf-8",
        )
        self.attempt = self.drill / "attempt.py"
        self.attempt.write_text("def double(x): return x + x\n", encoding="utf-8")

    def write_manifest(self):
        (self.drill / "tests.json").write_text(
            json.dumps(self.manifest), encoding="utf-8"
        )

    def run_cli(self, *args, env=None):
        return subprocess.run(
            [sys.executable, "-m", "tensor_drills.cli", *args],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            timeout=15,
        )

    def run_checker(self, drill_id="demo/double", *options):
        return self.run_cli("check", drill_id, "--workspace", str(self.root), *options)

    def test_repeated_checks_run_the_current_attempt(self):
        for _ in range(2):
            result = self.run_checker()
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PASS double two", result.stdout)

        self.attempt.write_text("def double(x): return x - x\n", encoding="utf-8")
        result = self.run_checker()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("FAIL double two", result.stdout)

    def test_wrong_answer_fails_when_python_optimization_is_enabled(self):
        self.attempt.write_text("def double(x): return 0\n", encoding="utf-8")
        result = self.run_cli(
            "check", "demo/double", "--workspace", str(self.root),
            env=dict(os.environ, PYTHONOPTIMIZE="1"),
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL double two", result.stdout)

    def test_external_attempt_can_be_checked_without_editing_starter(self):
        alternate = self.root / "other attempt.py"
        alternate.write_text("def double(x): return 2 * x\n", encoding="utf-8")
        self.attempt.write_text("raise ValueError('starter')\n", encoding="utf-8")

        result = self.run_checker("demo/double", "--attempt", str(alternate))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("starter", self.attempt.read_text(encoding="utf-8"))

    def test_exception_from_candidate_is_a_candidate_failure(self):
        self.attempt.write_text("def double(x): raise ValueError('attempt')\n")
        result = self.run_checker()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("ValueError: attempt", result.stdout)

    def test_missing_dependency_is_a_setup_error(self):
        self.manifest["dependencies"] = ["nonexistent_tensor_drill_dependency"]
        self.write_manifest()
        result = self.run_checker()
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("nonexistent_tensor_drill_dependency", result.stderr)

    def test_unknown_drill_is_a_setup_error(self):
        result = self.run_checker("demo/missing")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Unknown drill", result.stderr)

    def test_variant_uses_its_manifest_and_can_reuse_the_verifier(self):
        variant = self.drill / "variant"
        variant.mkdir()
        self.manifest["cases"] = [{"name": "double three", "inputs": 3, "expected": 6}]
        (variant / "tests.json").write_text(json.dumps(self.manifest), encoding="utf-8")
        shutil.copyfile(self.attempt, variant / "attempt.py")

        result = self.run_checker("demo/double", "--variant")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS double three", result.stdout)

    def test_init_copies_pilots_and_keeps_existing_attempts(self):
        workspace = self.root / "new workspace"
        result = self.run_cli("init", str(workspace))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((workspace / "README.md").is_file())
        follow_up = workspace / "drills/pytorch/inline-validation"
        for filename in ("prompt.md", "attempt.py", "tests.json", "verify.py", "rubric.md", "metadata.json"):
            self.assertTrue((follow_up / filename).is_file(), filename)

        starter = workspace / "drills/numpy/row-gather/attempt.py"
        starter.write_text("# in-progress attempt\n", encoding="utf-8")
        result = self.run_cli("init", str(workspace))
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(starter.read_text(encoding="utf-8"), "# in-progress attempt\n")
