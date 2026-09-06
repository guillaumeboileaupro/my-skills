import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(relative_path: str, *arguments: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / relative_path), *(str(argument) for argument in arguments)],
        text=True,
        capture_output=True,
        check=False,
    )


class SkillScriptTests(unittest.TestCase):
    def test_sqlite_preflight_handles_uri_metacharacters(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "data?#set.sqlite"
            with sqlite3.connect(database) as connection:
                connection.execute("CREATE TABLE sample (value INTEGER)")

            result = run_script(
                "skills/database-migration-safety/scripts/sqlite_preflight.py",
                database,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["tables"], ["sample"])
            self.assertEqual(list(Path(directory).iterdir()), [database])

    def test_release_audit_rejects_failed_checks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "release.json"
            manifest.write_text(
                json.dumps(
                    {
                        "version": "1.0.0",
                        "commit": "abc123",
                        "checks": {"tests": False},
                        "artifacts": [],
                    }
                ),
                encoding="utf-8",
            )

            result = run_script(
                "skills/release-readiness-audit/scripts/audit_manifest.py",
                manifest,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)["problems"], ["check:tests"])

    def test_evidence_matrix_accepts_top_level_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "evidence.json"
            requirements = Path(directory) / "requirements.txt"
            evidence.write_text(json.dumps(["Built reliable Python pipelines"]), encoding="utf-8")
            requirements.write_text("Python pipelines\n", encoding="utf-8")

            result = run_script(
                "skills/cv-evidence-tailoring/scripts/evidence_matrix.py",
                evidence,
                requirements,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("SUPPORTED: Python pipelines", result.stdout)

    def test_sample_check_rejects_column_without_finite_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            samples = Path(directory) / "samples.csv"
            samples.write_text("value\nNaN\ninvalid\ninf\n", encoding="utf-8")

            result = run_script(
                "skills/scientific-result-validation/scripts/check_samples.py",
                samples,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("value: n=0 invalid=3 no finite values", result.stdout)


if __name__ == "__main__":
    unittest.main()
