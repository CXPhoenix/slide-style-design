"""Structural checks at the published guidance seam, not model-behavior tests."""

from pathlib import Path
import re
import json
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "jobs-style"


class JobsGuidanceTests(unittest.TestCase):
    def test_named_style_has_a_direct_entry_and_accessible_references(self):
        entry = PACKAGE / "SKILL.md"
        text = entry.read_text(encoding="utf-8")
        header = text.split("---", 2)
        self.assertEqual(header[0], "")
        metadata = yaml.safe_load(header[1])
        self.assertEqual(metadata["name"], PACKAGE.name)
        self.assertIsInstance(metadata["description"], str)
        self.assertIn("Jobs", metadata["description"])
        for target in re.findall(r"\]\(([^)]+)\)", header[2]):
            if not re.match(r"^\w+://", target):
                self.assertTrue((PACKAGE / target).is_file(), target)

    def test_published_yaml_handoff_uses_the_agreed_core_contract(self):
        example = PACKAGE / "references" / "handoff-example.md"
        text = example.read_text(encoding="utf-8")
        blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
        self.assertEqual(len(blocks), 1)
        profile = yaml.safe_load(blocks[0])
        self.assertEqual(set(profile), {"style_id", "core_rules", "adjustable_rules"})
        self.assertEqual(profile["style_id"], "jobs")
        self.assertIsInstance(profile["core_rules"], list)
        self.assertIsInstance(profile["adjustable_rules"], list)
        identifiers = []
        for rule in profile["core_rules"] + profile["adjustable_rules"]:
            self.assertEqual(set(rule), {"rule_id", "constraint"})
            self.assertIsInstance(rule["rule_id"], str)
            self.assertRegex(rule["rule_id"], r"^[a-z][a-z0-9_.]*$")
            self.assertIsInstance(rule["constraint"], str)
            self.assertTrue(rule["constraint"].strip())
            identifiers.append(rule["rule_id"])
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertIn("jobs.single_focus", [r["rule_id"] for r in profile["core_rules"]])
        json.dumps(profile, allow_nan=False)

    def test_compatible_adjustment_example_has_core_and_non_core_settings(self):
        text = (PACKAGE / "references" / "compatible-example.md").read_text()
        blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
        self.assertEqual(len(blocks), 1)
        profile = yaml.safe_load(blocks[0])
        self.assertEqual(set(profile), {"style_id", "core_rules", "adjustable_rules"})
        self.assertEqual(profile["style_id"], "jobs")
        self.assertEqual([r["rule_id"] for r in profile["core_rules"]], ["jobs.text_primary"])
        self.assertEqual(len(profile["adjustable_rules"]), 1)
        identifiers = []
        for rule in profile["core_rules"] + profile["adjustable_rules"]:
            self.assertEqual(set(rule), {"rule_id", "constraint"})
            self.assertRegex(rule["rule_id"], r"^[a-z][a-z0-9_.]*$")
            self.assertIsInstance(rule["constraint"], str)
            self.assertTrue(rule["constraint"].strip())
            identifiers.append(rule["rule_id"])
        self.assertEqual(len(identifiers), len(set(identifiers)))
        json.dumps(profile, allow_nan=False)



    def test_conflict_example_returns_original_core_without_unaccepted_adjustment(self):
        text = (PACKAGE / "references" / "conflict-example.md").read_text()
        blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
        self.assertEqual(len(blocks), 1)
        profile = yaml.safe_load(blocks[0])
        self.assertEqual(set(profile), {"style_id", "core_rules", "adjustable_rules"})
        self.assertEqual(profile["style_id"], "jobs")
        self.assertEqual(len(profile["core_rules"]), 1)
        rule = profile["core_rules"][0]
        self.assertEqual(set(rule), {"rule_id", "constraint"})
        self.assertEqual(rule["rule_id"], "jobs.text_primary")
        self.assertIsInstance(rule["constraint"], str)
        self.assertTrue(rule["constraint"].strip())
        self.assertEqual(profile["adjustable_rules"], [])
        json.dumps(profile, allow_nan=False)

if __name__ == "__main__":
    unittest.main()
