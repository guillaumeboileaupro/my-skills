from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_skills


class ValidateSkillsTests(unittest.TestCase):
    def test_rejects_invalid_yaml_even_with_required_key_lines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "broken"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                '---\nname: "unterminated\ndescription: Something\n---\n', encoding="utf-8"
            )
            self.assertIn("invalid YAML frontmatter", "\n".join(validate_skills(Path(directory))))

    def test_rejects_non_mapping_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "list"
            skill.mkdir()
            (skill / "SKILL.md").write_text("---\n- name: example\n- description: A skill\n---\n", encoding="utf-8")
            self.assertIn("frontmatter must be a mapping", "\n".join(validate_skills(Path(directory))))

    def test_accepts_valid_yaml_with_quoted_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "valid"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                '---\nname: "example: skill"\ndescription: >\n  A useful skill.\n---\n', encoding="utf-8"
            )
            self.assertEqual(validate_skills(Path(directory)), [])


if __name__ == "__main__":
    unittest.main()
