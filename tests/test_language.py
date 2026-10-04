"""Published translation examples, not generated language behavior."""
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CORE = {"takahashi": "text_primary", "jobs": "single_focus", "wangxing": "text_visual_relation", "gates": "evidence_relation"}

class LanguageTests(unittest.TestCase):
    def test_english_examples_keep_stable_catalog_identifiers_and_constraint_types(self):
        for style, suffix in CORE.items():
            with self.subTest(style=style):
                text = (ROOT / "skills" / (style + "-style") / "references" / "english-example.md").read_text()
                blocks = re.findall(r"```yaml\n(.*?)\n```", text, re.S)
                self.assertEqual(len(blocks), 1)
                profile = yaml.safe_load(blocks[0])
                self.assertEqual(set(profile), {"style_id", "core_rules", "adjustable_rules"})
                self.assertEqual(profile["style_id"], style)
                self.assertEqual([x["rule_id"] for x in profile["core_rules"]], [style + "." + suffix])
                self.assertEqual([x["rule_id"] for x in profile["adjustable_rules"]], [style + ".presentation_preferences"])
                for rule in profile["core_rules"] + profile["adjustable_rules"]:
                    self.assertEqual(set(rule), {"rule_id", "constraint"})
                    self.assertIsInstance(rule["constraint"], str)
                    self.assertTrue(rule["constraint"].strip())

if __name__ == "__main__":
    unittest.main()
