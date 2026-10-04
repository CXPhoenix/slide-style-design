"""Published boundary examples, not LLM behavior."""
from pathlib import Path
import re, unittest, yaml
ROOT = Path(__file__).resolve().parents[1]
class MaterialBoundaryTests(unittest.TestCase):
    def test_every_independent_entry_exposes_a_boundary_example(self):
        for name in ['takahashi-style','jobs-style','wangxing-style','gates-style','presentation-style-route']:
            package = ROOT / 'skills' / name
            entry = (package / 'SKILL.md').read_text()
            self.assertIn('(references/material-boundary.md)', entry)
            text = (package / 'references/material-boundary.md').read_text()
            records = yaml.safe_load(re.findall(r'```yaml\n(.*?)\n```', text, re.S)[0])
            self.assertEqual(records['quoted_commands']['controls'], 'caller')
            self.assertEqual(records['quoted_commands']['material_context'], 'usable')
            self.assertEqual(records['explicit_adoption']['controls'], 'adopted_caller')
            self.assertEqual(records['explicit_adoption']['core_and_scope'], 'unchanged')
