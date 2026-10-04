# T-0011 test plan

Continuous implementation plans and browser ChatGPT conversations approved 2026-10-04. Concrete plan before tests. Two objectives, existing S1 published-doc and S2 real-conversation seams.

| Plan | Seam / scope | Boundary / expected | Scoped AC | Evidence |
|---|---|---|---|---|
| TP01 | S1 focus-anchor branch examples | Fixed AI concept→Wangxing, measuredenergy→Gates, productbenefit+quantitativecomparison→Jobs/Gates; one eligible, no uniquewinner/alloptionalfields requirement | AC-07/09 | One bounded published branch-example test, semantic review |
| TP02 | S1 missingcontext example | Generic / audiencealone lack purpose/expression anchor; no fabricatedprofile | AC-08/15 | One example shape test + semantic review |
| TP03 | S2 CT01–03 actual selection | Suppliedpurpose/expression matches focus; reason names anchor+chosenfocus, oneprofile no optionalquestions, no invented expertise/humor/venue | AC-07/09/15/18/19 | Full original answers, profile parsing, manual reason/core checks |
| TP04 | S2 CT04–05 clarification | Ask missingpurpose/expression only in callerlanguage, no chosenstyle/profile/inventedfacts | AC-08/15/18/19 | Full original answer, semantic verdict |

CT01:
> 透過 presentation-style-route 幫我選風格。我想向高中生介紹 AI，沒有指定風格，也沒有另外提供表達需求或場地。只提供風格指引與設定，不改寫或製作內容。用台灣繁體中文。
CT02:
> Through presentation-style-route, choose one style for comparing measured energy use. I give no separate audience or venue. Provide style guidance and settings in English, without calculation, rewriting or production.
CT03:
> 透過 presentation-style-route 選一個主要風格：用途是說明產品效益，同時比較量測得到的用電量。我沒有唯一偏好，不補充觀眾或場地。提供理由、風格指引與 JSON 設定，不計算或改寫素材。用台灣繁體中文。
CT04:
> 透過 presentation-style-route 幫我選簡報風格。
CT05:
> Through presentation-style-route, choose a presentation style. The audience is teachers. Reply in English.

Selection oracle is approved focusanchors, not statisticalbenefit or uniquebeststyle. Use selectedstyle catalog for deliveredcore, conditionalnecessaryqualifiers retained even facts absent. Earlier explicitchoice precedence stays. Actualcases one perversion; preserve failures/correctcandidate/rerunaffected, one technicalretry. MCP unverified, quotedcommands/unresolvednames later work.
