# T-0001 coverage report

Status: closed after scoped checks passed and local no-ff landing `125bf9f` on 2026-10-04.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Jobs entry/reference check passed | 1/1 structural check | AC-05, AC-16 | Actual invocation covered by TP-04; exact model ID unknown |
| S1 / TP-02 | Core/source compared with accepted spec; independent product review passed | Semantic coverage not numerically measured | AC-03, AC-04, AC-20 | Actual response covered by TP-04/05; no numerical semantic coverage claim |
| S1 / TP-03 | Jobs YAML check passed; manual meaning comparison | 1/1 structural check; semantic coverage not numerically measured | AC-12–AC-14 | Actual response contract checked in TP-04/05 |
| S2 / TP-04 | CT-01 input, response and per-check verdict retained | 1/1 passed responses | AC-03, AC-05, AC-12–AC-16, AC-18 | Exact default model ID unknown; no independently exported submitted input |
| S2 / TP-05 | CT-02 input, response and per-check verdict retained | 1/1 passed responses | AC-02, AC-03, AC-12, AC-14, AC-18, AC-20 | Exact default model ID unknown; no independently exported submitted input |
| S1/S2 / TP-06 | Input/response hashes, fixed requests, available host details and verdicts retained | Planned evidence retained; not numerically measured | AC-18, AC-19 | Exact default model ID unknown; no failure or retry reported |

No document check proves model behavior. Skills MCP loading remains unverified.
JSON, language expansion, adjustments and route are outside T-0001.

Full suite: four tests passed ([log](full-suite.log)); portable verifier and scoped diff check passed. Independent review results: [change](change-review.md), [security](../../../../.proj.specs/0001-style-guidance/review/security-T-0001.md).

Actual response audit: [trial-results.md](trial-results.md).
