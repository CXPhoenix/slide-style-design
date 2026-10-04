# T-0007 final coverage reconciliation

2026-10-04 T14 audit: final actual CT01/02 both passed, one planned run each.
See chatgpt-results.md and trial-manifest.json for response/input revision evidence.

| Seam | Tests | Measured coverage | AC | Uncovered / why |
|---|---|---|---|---|
| S1 | 16 full-suite local checks plus manual record review | Two published boundary profiles checked | 03/04/10–14/20 | Model behavior separate |
| S2 | CT01 compatible; CT02 conflict | 2/2 actual trials passed | Scoped plan AC | MCP/JSON/language/route outside original slice |

## Historical pre-trial table (retained)

# T-0007 coverage report

Status: local candidate, actual trials pending.

| Seam / plan | Evidence | Measured coverage | AC | Uncovered / why |
| --- | --- | --- | --- | --- |
| S1 TP-01 | Optional source/rule conditions/examples inspected | 1 rule inspected; no semantic percentage | AC-03/04/14/20 | Model attribution pending |
| S1 TP-02 | Compatible public YAML + meaning review | 1/1 structure pass | AC-10/12/14 | Actual response pending |
| S1 TP-03 | Conflict public YAML + meaning review | 1/1 structure pass | AC-11–14 | Actual response pending |
| S2 TP-04 | CT-01 prepared | 0/1 executions | Plan scoped AC | Browser response pending |
| S2 TP-05 | CT-02 prepared | 0/1 executions | Plan scoped AC | Browser response pending |
| S1/S2 TP-06 | Input/product hashes | Partial | AC-18/19 | Reply/URL/effort/verdict pending |

Full16 tests pass; verifier/whitespace pass. No static result proves ChatGPT behavior. MCP/JSON/language/route outside scope.

Actual CT-01/02: both passed semantic review and YAML parsing; see chatgpt-results.md and trial-manifest.json. Skills MCP unverified.
