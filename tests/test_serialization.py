"""Published example contract, not model behavior."""
import json
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CORE = {"takahashi": "text_primary", "jobs": "single_focus", "wangxing": "text_visual_relation", "gates": "evidence_relation"}

class SerializationTests(unittest.TestCase):
    def test_explicit_json_examples_preserve_the_existing_catalog_contract(self):
        for style, suffix in CORE.items():
            with self.subTest(style=style):
                package = ROOT / "skills" / (style + "-style") / "references"
                original = yaml.safe_load(re.findall(r"```yaml\n(.*?)\n```", (package / "compatible-example.md").read_text(), re.S)[0])
                text = (package / "json-example.md").read_text()
                blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
                self.assertEqual(len(blocks), 1)
                self.assertNotIn("```yaml", text)
                profile = json.loads(blocks[0])
                self.assertEqual(profile, original)
                self.assertEqual(set(profile), {"style_id", "core_rules", "adjustable_rules"})
                self.assertEqual(profile["core_rules"][0]["rule_id"], style + "." + suffix)
                self.assertEqual(len(profile["adjustable_rules"]), 1)

if __name__ == "__main__":
    unittest.main()
