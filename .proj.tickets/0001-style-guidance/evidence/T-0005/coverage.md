# T-0005 coverage report

Status: done after landing, merge d21816fa0add33d7be19e49d9bf964fb80aca71e.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Adjustable source/classification/conditions/examples inspection | One new adjustable record inspected; no semantic percentage | AC-03, AC-04, AC-14, AC-20 | Actual response attribution pending |
| S1 / TP-02 | Compatible public YAML example check + meaning comparison | 1/1 structural check passed | AC-10, AC-12, AC-14 | Actual application pending CT-01 |
| S1 / TP-03 | Conflict public YAML example check + meaning comparison | 1/1 structural check passed | AC-11–AC-14 | Actual conflict response pending CT-02 |
| S2 / TP-04 | CT-01 versioned input prepared | 1/1 execution passed | AC-02–AC-05, AC-10, AC-12–AC-14, AC-18–AC-20 | Assistant-operated actual ChatGPT passed; exact model not shown |
| S2 / TP-05 | CT-02 versioned input prepared | 1/1 execution passed | AC-02–AC-05, AC-11–AC-14, AC-18–AC-20 | Assistant-operated actual ChatGPT passed; exact model not shown |
| S1/S2 / TP-06 | Requests/product/input hashes prepared | Partial, not numerical | AC-18, AC-19 | Full replies/hash/URL/Medium/verdict recorded; exact model unknown |

Full suite 12 passed after fixture correction (corrected-full-suite.log); original full-suite.log failed and remains archived; existing core entry and core-only handoff checks unchanged and passed. Portable verifier passed. No local check proves ChatGPT behavior. Skills MCP, route, JSON switching and language expansion remain unverified/outside this ticket.

Original claimed greens were fixture failures; preserved in pre-review-correction. Corrected-affected.log: 4 passed. Corrected-full-suite.log: 12 passed. Current prepared trial candidate 02, both actual cases pending; candidate 01 was never submitted.

Actual candidate02 CT-01/CT-02 each executed once, passed all approved checks. Screenshots and full replies retained. MCP unverified. Independent review findings resolved; duplication smell non-blocking.
