# T-0009 coverage

| Seam / plan | Evidence | Measured coverage | Scoped AC | Uncovered / reason |
|---|---|---|---|---|
| S1 TP-01 | English public examples IDs/types | 1/1 test; 4/4 styles | AC-05/12/14/15/16 | Actual language behavior needs S2 |
| S1 semantic meaning | Four translations preserve core/optional relations and supplied restrictions | 4/4 inspected, no semantic percentage | AC-12/14/15 | No arbitrary-language guarantee |
| S2 TP-02 | English Wangxing accepted request | 1/1 executions, pass | AC-12/14/15/18/19 | Full reply/hash/screenshot retained |
| S2 TP-03 | Chinese Takahashi conflict request | 1/1 executions, pass | AC-11/12/14/15/18/19 | Full reply/hash/screenshot retained |
| Later routes / MCP | None | Unverified | AC-15/16/19 | Separate route/release/loading surfaces |

Full18 local tests, portable verifier and whitespace checks pass. No local check proves ChatGPT behavior.
