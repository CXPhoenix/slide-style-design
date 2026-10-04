# T-0000 coverage report

Status: T-0000 scoped checks passed; landing recorded separately.

| Plan / seam | Tests / evidence | Measured coverage | Acceptance criterion | Uncovered, and why |
| --- | --- | --- | --- | --- |
| TP-01 / S1 entry | Metadata/reference existence test passed; independent Standards/Spec reviews | 1/1 planned structural check; semantic coverage not numerically measured | AC-05, AC-16 | Actual model invocation belongs to TP-04 |
| TP-02 / S1 core/source | Accepted propositions compared with core/source record; independent Spec review, zero findings | Semantic coverage not numerically measured | AC-03, AC-04, AC-20 | Actual response semantics require TP-04/05; no fresh external-source verification in this review |
| TP-03 / S1 YAML | Parse/schema/ID/type test passed; independent semantic document review | 1/1 planned structural check; semantic coverage not numerically measured | AC-12, AC-13, AC-14 | Response-generated YAML requires actual ChatGPT |
| TP-04 / S2 CT-01 | Versioned input, user-supplied complete response, structure and semantic verdict recorded | 1/1 planned ChatGPT executions passed | AC-05, AC-12–AC-15, AC-18 | Exact default model identifier and independently exported submitted input unavailable |
| TP-05 / S2 CT-02 | Versioned input, user-supplied complete response, structure and semantic verdict recorded | 1/1 planned ChatGPT executions passed | AC-02, AC-03, AC-12, AC-14, AC-18 | Exact default model identifier and independently exported submitted input unavailable |
| TP-06 / S1/S2 evidence | Input/response SHA-256, fixed requests, available host/model/effort and verdict recorded | Planned evidence retained; evidence coverage not numerically measured | AC-18, AC-19 | No failure/retry reported; exact model ID unknown; supplied responses are user-operated evidence |

No model-behavior coverage percentage is inferred from document checks. Skills MCP
loading is separately unverified. JSON, multilingual variants, adjustments, and
routing are outside T-0000. Red/green logs are linked in [tdd.md](tdd.md).
The full existing product suite passed (two tests), the portable project verifier
passed, and tracked diff whitespace checks passed on 2026-10-03. See
[local verification](local-verification.log) and [change review](change-review.md).

Actual-surface evidence: [trial results](trial-results.md), [CT-01](CT-01-response.md), [CT-02](CT-02-response.md).
