# T-0012 approved test plan

2026-10-04 continuous-run approval applies to the unchanged S1 published-document
and S2 actual ChatGPT seams. Two objectives; concrete table written before tests.

| Plan | Seam / intent | Scope / boundary | Scoped AC | Evidence |
|---|---|---|---|---|
| TP01 | S1 named-choice clarification examples | Ambiguous/unsupported explicit name asks intended supported style even when purpose fits; no invented preset/profile | AC-08/15 | One public branch-metadata test and semantic review |
| TP02 | S1 multiple-choice examples | Multiple/per-page mixing asks one primary style; after selection preserve explicit route and requested language/format | AC-09/15/18 | One public branch-metadata test and semantic review |
| TP03 | S2 actual clarification | CT01–04 no fabricated profile; concise supported-choice question in caller language, purpose cannot override unresolved explicit preference | AC-08/09/15/18/19 | Original response, browser evidence and semantic verdict |
| TP04 | S2 resolved continuation | CT05 reply to CT03 selects Jobs and delivers real guidance with original JSON/language preference | AC-08/09/15/18/19 | Original two-turn conversation, profile parser and catalog review |

CT01:
> 透過 presentation-style-route 使用「蘋果流」。用途是比較量測得到的用電量。請用台灣繁體中文回覆，只提供風格約束。
CT02:
> Use Tufte style through presentation-style-route to compare measured energy use. Reply in English and provide style constraints only.
CT03:
> 透過 presentation-style-route 同時使用高橋流與賈伯斯流，提供風格約束與 JSON 設定。請用台灣繁體中文。
CT04:
> Through presentation-style-route, automatically use Jobs for product pages and Gates for data pages. Reply in English; provide style constraints only.
CT05:
> 我選賈伯斯流作為唯一主要風格，沿用 JSON 與台灣繁體中文。請依已提供的 jobs-style 指引給我風格約束，不改寫內容。

No missing optional-field requirement, new preset, actual mixing or production is
introduced. Skills MCP loading remains unverified; supplied definitions demonstrate
conversation behavior only. Preserve original technical failures and candidates.
