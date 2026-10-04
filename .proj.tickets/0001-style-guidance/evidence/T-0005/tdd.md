# T-0005 TDD evidence — corrected record

User continuous-execution approval preceded the concrete plan and tests. Scope: compatible preferences and core conflict, existing S1/S2. Cycle 1 missing compatible public example was red; cycle 2 missing conflict example was red. Minimal implementations were made separately, but reused test fixtures erroneously expected jobs.text_primary instead of approved jobs.single_focus. Therefore initial green-01, green-02 and full-suite logs were failures, not greens; prior passing claims were incorrect. Complete original logs, fixture, claims and inputs preserved in pre-review-correction/. Do not treat the original sequence as a clean red/green loop.

Review correction: fix test oracle to the existing approved core ID, retain correct product ID. Changed Chinese lunch wording to 選單 before actual submission; no ChatGPT response exists for the earlier prepared input. Corrected affected/full checks recorded separately. Semantic inspection against AC-10/11 confirms one focal point/supporting relation, requested color/four products/test-specific limit in compatible settings; conflict ID/request/broken relation/suggestion, original core and no applied alternative in conflict settings. Document meaning review is not actual model verification.

Actual CT-01/02 pending. Skills MCP unverified. No commit/landing until reviews and actual cases pass.
