# T-0012 coverage

| Seam / plan | Tests | Measured coverage | Scoped AC | Uncovered / why |
|---|---|---|---|---|
| S1 TP01 | Published named-choice branch test | 1/1; ambiguous and unsupported examples inspected | AC-08/15 | Model behavior requires S2 |
| S1 TP02 | Published multi-choice branch test | 1/1; multiple/per-page/resolved examples inspected | AC-09/15/18 | Model behavior requires S2 |
| S2 TP03 | Actual CT01–04 | 4/4 passed | AC-08/09/15/18/19 | Original browser response verified |
| S2 TP04 | Actual CT05 continuation | 1/1 passed | AC-08/09/15/18/19 | Original browser response verified |
| MCP | None | Unverified | AC-19 | Separate loading compatibility |

Full local suite: 24 passed. Static examples validate published branch documentation,
not a runtime classifier, actual skill loading or universal model reliability.

Actual branch/continuation evidence: actual-results.md and trial-manifest.json.
