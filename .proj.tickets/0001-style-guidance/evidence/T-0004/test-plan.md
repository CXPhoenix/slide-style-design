# T-0004 test plan

Status: approved by user reply A on 2026-10-04.
Date: 2026-10-04. Base main: 6e8e64c. Branch: tickets/T-0004/takahashi-adjustments.
Accepted specification/matrix hashes checked unchanged. T-0000 done.

## Scope and seams

Two objectives only: compatible non-core Takahashi adjustments; conflict explanation retaining original core. Existing S1 published Markdown/YAML boundary and S2 user-operated actual ChatGPT response boundary. Reuse existing entry/reference/YAML structural checks. No production, content restructuring, route, JSON switching or language expansion.

| ID | Seam | Test intent / independent oracle | Scope | AC / boundary |
| --- | --- | --- | --- | --- |
| TP-01 | S1 rule records | Inspect every declared adjustable rule's fixed ID, classification, source/inference basis, limits and compatible/conflicting examples | Source/document review against approved spec and existing T1/T2 evidence; no new creator formula | AC-03, AC-04, AC-14, AC-20; adjustment options are project synthesis, not creator mandates |
| TP-02 | S1 compatible handoff | Accepted supporting chart/three note lines appear in Markdown/settings while all three core propositions and supplied scope limit remain | One bounded public YAML example check plus semantic review | AC-10, AC-12, AC-14; no numeric count threshold; chart presence/count alone is not conflict |
| TP-03 | S1 conflict handoff | Identify core ID, conflicting request, broken proposition and retaining suggestion; preserve original core; settings omit override and unaccepted alternative | One bounded public YAML example check plus semantic review | AC-11–AC-14; suggestion is explanation, not accepted settings; do not replace style or create a permission workflow |
| TP-04 | S2 CT-01 | Actual compatible request accepted directly; chart/notes stay subordinate; relative text scale and source qualification preserved in both representations | One fresh ChatGPT conversation; full structural/semantic audit | AC-02–AC-05, AC-10, AC-12–AC-14, AC-18–AC-20 |
| TP-05 | S2 CT-02 | Actual core replacement explained; original text priority and conditional supporting relation retained; conflicting request and suggested alternative absent from applied settings | One separate fresh ChatGPT conversation; full structural/semantic audit | AC-02–AC-05, AC-11–AC-14, AC-18–AC-20 |
| TP-06 | S1/S2 evidence | Preserve candidate inputs/product hashes/full responses/model/effort/verdicts/failures/reruns | Evidence review; local checks distinct from actual ChatGPT and MCP | AC-18, AC-19; unavailable exact model unknown |

## Fixed actual ChatGPT cases

### CT-01 — Compatible chart/notes

> 請使用高橋流提供現場投影的風格指引與設定。我想加入一張輔助圖表與三行註解，兩者都只支援主要詞句，不成為同等或更強的焦點；主要詞句仍透過相對尺度保持優先。素材中的「結果僅適用於本次測試條件」是理解所必需的限定，請保留。只提供風格指引，不改寫或重組素材。以台灣繁體中文回覆。

Expected: directly accept adjustment; Markdown and YAML preserve text primary, relative-scale priority and conditional subordinate detail. Chart and three note lines explicitly reflected as accepted non-core guidance, not rejected by presence/count or declared creator-count rule. Qualification stays in both representations. Style takahashi, mandatory takahashi.text_primary, exactly one parseable YAML with agreed fields and unique nonempty English rule_id/nonempty string constraints. Declared non-core IDs stable from published rule records; settings reflect accepted changes. No page plan, moving material, rewrite or production.

### CT-02 — Core replacement; alternative unaccepted

> 請使用高橋流提供現場投影的風格指引與設定，但我要讓密集圖表成為主要視覺與訊息載體，詞句只當小標題。素材中的「結果僅適用於本次測試條件」仍必須保留。我尚未同意任何替代方案；請說明衝突並提出保留高橋流核心的建議，設定維持原本核心，不套用我的衝突要求，也不把你提出的替代方案視為已接受。只提供風格指引，不改寫或重組素材。以台灣繁體中文回覆。

Expected: name takahashi.text_primary, paraphrase requested dense-chart dominance/minor words, explain broken text primary/relative priority/subordinate relation, offer a compatible retaining suggestion in Markdown. Deliver original core and necessary supplied qualifier in both representations, not merely refusal. Settings exclude conflicting override and unaccepted alternative. No auto-switch style, new production flow or request for permission needed to deliver original guidance. Exactly one valid agreed YAML.

## Execution / retry policy

User manually operates ChatGPT: two fresh chats, complete versioned entry and needed references inline, one case per chat. Same default model/medium; record visible labels, unknown exact model stays unknown. Preserve prepared input separately from independently captured submitted input (if any). All required checks must pass each case. Actual incorrect response is a failure: retain complete response, correct skill and create new candidate hash, rerun both unchanged cases. Technical undelivered/interrupted run remains unverified; at most one technical retry per case/candidate, retained. No arbitrary passing selection from multiple outputs. Skills MCP loading separately unverified.

## TDD / completion

After approval: record missing compatible behavior as semantic red against published spec; add one bounded compatible public-example structure check and minimal guidance/example, then inspect meaning against oracle. Repeat for conflict branch as separate cycle. Meaning judged from propositions/conditions, not exact prose/keyword assertions. Reuse unittest/PyYAML, no framework or renderer. Run affected checks each cycle and full suite once at completion; portable verifier; scoped whitespace check. Record coverage table with unmeasured/uncovered boundaries. Independent Standards/Spec and security reviews, actual trials, skill-generated commit/landing; done after landing. Do not close from static checks.

## 使用者審核

A：核准全部計畫與兩案；B：指定編號修改；C：指定編號補充說明。
