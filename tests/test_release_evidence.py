"""Audit delivered evidence links and candidate integrity, not model compliance."""
from pathlib import Path
import hashlib, json, unittest
ROOT = Path(__file__).resolve().parents[1]
class ReleaseEvidenceTests(unittest.TestCase):
    def test_release_candidate_and_every_ac_have_resolvable_evidence(self):
        path = ROOT / '.proj.tickets/0001-style-guidance/evidence/T-0014/release-manifest.json'
        m = json.loads(path.read_text())
        self.assertEqual(m['skills_mcp_status'], 'unverified')
        self.assertEqual(set(m['criteria']), {f'AC-{i:02d}' for i in range(1,21)})
        self.assertEqual(set(m['product_files']), {str(p.relative_to(ROOT)) for p in (ROOT/'skills').rglob('*.md')})
        for name, digest in m['product_files'].items():
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), digest)
        for criterion in m['criteria'].values():
            self.assertTrue(criterion['document_evidence'])
            for name in criterion['document_evidence']:
                self.assertTrue((ROOT/name).is_file(), name)
            for case in criterion['actual_cases']:
                source = ROOT / case['manifest']
                record = next(c for c in json.loads(source.read_text())['cases'] if c['case_id']==case['case_id'])
                self.assertEqual(record['status'], 'passed')
                self.assertTrue((source.parent/record['input_file']).is_file())
                response = source.parent/record['response_file']
                self.assertEqual(hashlib.sha256(response.read_bytes()).hexdigest(), record['response_sha256'])
                self.assertTrue(case['applicability'])
