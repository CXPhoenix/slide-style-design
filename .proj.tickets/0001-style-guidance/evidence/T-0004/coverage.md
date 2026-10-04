# T-0004 coverage report

Status: complete; landed on main via merge `5eb2f99ed41700997b6e72a287f3f1c0a1b3fd17`, ticket done after landing.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Adjustable source/classification/conditions/examples inspection | One new adjustable record inspected; no semantic percentage | AC-03, AC-04, AC-14, AC-20 | Catalog attribution inspected; pasted-text citations not independently resolved |
| S1 / TP-02 | Compatible public YAML example check + meaning comparison | 1/1 structural check passed | AC-10, AC-12, AC-14 | CT-01 passed; general reliability not measured |
| S1 / TP-03 | Conflict public YAML example check + meaning comparison | 1/1 structural check passed | AC-11–AC-14 | CT-02 passed; general reliability not measured |
| S2 / TP-04 | CT-01 versioned input prepared | 1/1 execution passed | AC-02–AC-05, AC-10, AC-12–AC-14, AC-18–AC-20 | Full user-supplied reply audited; exact model unknown |
| S2 / TP-05 | CT-02 versioned input prepared | 1/1 execution passed | AC-02–AC-05, AC-11–AC-14, AC-18–AC-20 | Full user-supplied reply audited; exact model unknown |
| S1/S2 / TP-06 | Requests/product/input hashes prepared | Partial, not numerical | AC-18, AC-19 | Full replies/hash/verdict/default model/medium recorded; submitted-input/platform log not independently captured |

Full suite 10 passed; existing core entry and core-only handoff checks unchanged and passed. Portable verifier passed. No local check proves ChatGPT behavior. Skills MCP, route, JSON switching and language expansion remain unverified/outside this ticket.

Independent Standards/Spec review: zero actionable findings, one non-blocking duplication smell. Security review: zero HIGH/MEDIUM candidates. Snapshot drift check passed; actual trials now passed.

Actual surface: user-operated ChatGPT inline loading. CT-01 and CT-02 each executed once and passed all approved checks. No failed run or rerun reported. Exact model unknown; Skills MCP remains unverified.
