# T-0002 coverage report

Status: closed after scoped checks passed and local no-ff landing `b1fd32e` on 2026-10-04.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Entry/reference check passed | 1/1 structural check | AC-05, AC-16 | Invocation covered by TP-04; exact model ID unknown |
| S1 / TP-02 | Core/source compared with accepted propositions | Semantic coverage not numerically measured | AC-03, AC-04, AC-20 | Document and response meaning reviewed; numerical semantic coverage not measured |
| S1 / TP-03 | Published YAML check and manual semantics passed | 1/1 structural check; meaning not numerically measured | AC-12–AC-14 | Actual settings covered by TP-04/05 |
| S2 / TP-04 | CT-01 versioned input, response and verdict retained | 1/1 passed responses | AC-03, AC-05, AC-12–AC-16, AC-18 | Exact model ID unknown; submission not independently exported |
| S2 / TP-05 | CT-02 versioned input, response and verdict retained | 1/1 passed responses | AC-02, AC-03, AC-04, AC-12, AC-14, AC-18, AC-20 | Exact model ID unknown; submission not independently exported |
| S1/S2 / TP-06 | Request/content/response hashes, reported host/model/effort and verdicts retained | Planned evidence retained; not numerically measured | AC-18, AC-19 | No failure/retry reported; exact model ID unknown |

Document checks do not prove model behavior. MCP loading is separately unverified.
JSON, other language variants, adjustment handling and route are outside T-0002.

Full suite: 6 tests passed ([log](full-suite.log)); portable verifier and tracked diff check passed. [Change review](change-review.md) has no documented/spec findings and one non-blocking duplication smell; [security review](../../../../.proj.specs/0001-style-guidance/review/security-T-0002.md) has zero qualifying candidates.

Actual trial audit: [results](trial-results.md).
