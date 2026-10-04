# T-0003 coverage report

Status: complete; landed on local main via merge `26267d9b32f9f70f8cff087cd6d4b8f38a0f24fa`. Ticket done after landing.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Entry/reference structure check | 1/1 check passed | AC-05, AC-16 | General invocation reliability not measured |
| S1 / TP-02 | Source/core review; independent Spec review | Both core propositions inspected; no numerical semantic metric | AC-03, AC-04, AC-20 | Source video visuals/timing not inspected |
| S1 / TP-03 | Handoff YAML check; meaning review | 1/1 check passed | AC-12–AC-14 | Other styles' future adjustments outside scope |
| S2 / TP-04 | Actual CT-01 candidate 02 | 1/1 execution passed; all required checks passed | AC-03, AC-05, AC-12–AC-16, AC-18 | Two cases do not prove general reliability |
| S2 / TP-05 | Actual CT-02 candidate 02 | 1/1 execution passed; all required checks passed | AC-02–AC-04, AC-12, AC-14, AC-18, AC-20 | No general benchmark or renderer verification |
| S1/S2 / TP-06 | Full inputs/product hashes/replies/verdicts/history | Both current cases recorded; candidate 01 retained | AC-18, AC-19 | Exact model unknown; no independent submitted-input capture or platform log; MCP not tested |

Candidate 01 CT-01 failed scope; CT-02 passed. Candidate 02 reran both and passed.
Both candidates used default model/medium according to the user. Failure retention
and unchanged requests inspected by independent targeted reviews. Full suite:
8 passed; portable verifier passed. Standards/spec zero actionable findings;
security zero HIGH/MEDIUM candidates; existing test duplication smell non-blocking.
Actual trials are user-operated ChatGPT inline loading, not Skills MCP loading.
JSON, language expansion, adjustments and route remain later tickets.
