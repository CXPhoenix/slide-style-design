"""Published route links/examples, not model selection behavior."""
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "presentation-style-route"

class RouteTests(unittest.TestCase):
    def test_explicit_route_registry_resolves_the_four_actual_style_entries(self):
        text = (PACKAGE / "SKILL.md").read_text()
        header = text.split("---", 2)
        self.assertEqual(yaml.safe_load(header[1])["name"], "presentation-style-route")
        for target in re.findall(r"\]\(([^)]+)\)", header[2]):
            if not re.match(r"^\w+://", target):
                self.assertTrue((PACKAGE / target).is_file(), target)
        registry = PACKAGE / "references" / "styles.md"
        blocks = re.findall(r"```yaml\n(.*?)\n```", registry.read_text(), re.S)
        self.assertEqual(len(blocks), 1)
        records = yaml.safe_load(blocks[0])
        self.assertEqual(set(records), {"takahashi", "jobs", "wangxing", "gates"})
        for style, entry in records.items():
            target = (registry.parent / entry).resolve()
            self.assertEqual(target, ROOT / "skills" / (style + "-style") / "SKILL.md")
            metadata = yaml.safe_load(target.read_text().split("---", 2)[1])
            self.assertEqual(metadata["name"], style + "-style")

    def test_unavailable_guidance_example_reports_a_limit_without_a_fabricated_profile(self):
        text = (PACKAGE / "references" / "unavailable-example.md").read_text()
        self.assertFalse(re.findall(r"```(?:yaml|json)\n", text))
        self.assertNotIn("core_rules:", text)
        self.assertNotIn('"core_rules"', text)

    def test_published_context_examples_follow_the_spec_focus_anchor_branches(self):
        text = (PACKAGE / "references" / "context-examples.md").read_text()
        examples = yaml.safe_load(re.findall(r"```yaml\n(.*?)\n```", text, re.S)[0])
        self.assertEqual(set(examples), {"ai_concept", "measured_energy", "multiple_anchors"})
        self.assertEqual(examples["ai_concept"]["eligible_styles"], ["wangxing"])
        self.assertEqual(examples["measured_energy"]["eligible_styles"], ["gates"])
        self.assertEqual(set(examples["multiple_anchors"]["eligible_styles"]), {"jobs", "gates"})
        for example in examples.values():
            self.assertEqual(example["branch"], "deliver_one_eligible")
            self.assertIsInstance(example["request"], str)

    def test_missing_context_examples_do_not_fabricate_a_style_profile(self):
        text = (PACKAGE / "references" / "missing-context-example.md").read_text()
        self.assertFalse(re.findall(r"```(?:yaml|json)\n", text))
        self.assertNotIn("core_rules:", text)
        self.assertNotIn('"core_rules"', text)

    def test_named_choice_examples_clarify_within_the_supported_set(self):
        text = (PACKAGE / "references" / "choice-examples.md").read_text()
        records = yaml.safe_load(re.findall(r"```yaml\n(.*?)\n```", text, re.S)[0])
        for key in ("ambiguous", "unsupported"):
            self.assertEqual(records[key]["branch"], "ask_supported_choice")
            self.assertEqual(records[key]["settings"], None)
            self.assertEqual(set(records[key]["supported_styles"]),
                             {"takahashi", "jobs", "wangxing", "gates"})

    def test_multiple_style_examples_require_one_primary_before_delivery(self):
        text = (PACKAGE / "references" / "choice-examples.md").read_text()
        records = yaml.safe_load(re.findall(r"```yaml\n(.*?)\n```", text, re.S)[0])
        for key in ("multiple", "per_page"):
            self.assertEqual(records[key]["branch"], "ask_one_primary")
            self.assertIsNone(records[key]["settings"])
        self.assertEqual(records["resolved"]["branch"], "deliver_explicit")
        self.assertEqual(records["resolved"]["style_id"], "jobs")

if __name__ == "__main__":
    unittest.main()
