# T-0005 coverage report

Status: local candidate; not closure.

| Seam / plan | Tests / evidence | Measured coverage | AC | Uncovered, and why |
| --- | --- | --- | --- | --- |
| S1 / TP-01 | Adjustable source/classification/conditions/examples inspection | One new adjustable record inspected; no semantic percentage | AC-03, AC-04, AC-14, AC-20 | Actual response attribution pending |
| S1 / TP-02 | Compatible public YAML example check + meaning comparison | 1/1 structural check passed | AC-10, AC-12, AC-14 | Actual application pending CT-01 |
| S1 / TP-03 | Conflict public YAML example check + meaning comparison | 1/1 structural check passed | AC-11–AC-14 | Actual conflict response pending CT-02 |
| S2 / TP-04 | CT-01 versioned input prepared | 0/1 executions | AC-02–AC-05, AC-10, AC-12–AC-14, AC-18–AC-20 | User-operated ChatGPT pending |
| S2 / TP-05 | CT-02 versioned input prepared | 0/1 executions | AC-02–AC-05, AC-11–AC-14, AC-18–AC-20 | User-operated ChatGPT pending |
| S1/S2 / TP-06 | Requests/product/input hashes prepared | Partial, not numerical | AC-18, AC-19 | Full replies/model/effort/verdict absent |

Full suite 12 passed; existing core entry and core-only handoff checks unchanged and passed. Portable verifier passed. No local check proves ChatGPT behavior. Skills MCP, route, JSON switching and language expansion remain unverified/outside this ticket.
