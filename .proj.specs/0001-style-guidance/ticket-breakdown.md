# Approved ticket breakdown — style guidance

Status: approved and published; revision 2; granularity, blocking edges, and deliverables approved on 2026-10-03.
Created and revised: 2026-10-03.

Sources: [accepted specification](spec.en.md), [traceability](traceability.md), [completed user specification review](user-review.md), and [technical review acceptance](review/accepted.json).
Accepted English specification SHA-256: `e9aa76437e72a36ca4ed1832e2d856bc48bc7a2ea8aad0ac63112c721d2acef1`.

The [previous seven-ticket proposal](ticket-breakdown-v1.md) is retained and superseded. No breakdown category was approved for that proposal. The user clarified that a ticket's reflection/audit should cover at most one or two functions or structural changes. This revision adopts that limit without changing the accepted product specification.

Permanent IDs T-0000–T-0014 were allocated after rescanning the complete tracker and finding no existing tickets. The approved slices are now published as individual ticket files.

## Scope accounting

- Each ticket declares one or two independently auditable change objectives: an observable capability or a coherent structural change.
- New adjustment, serialization, language, or routing capabilities cannot be hidden inside the broad label “complete a style.”
- Source attribution, explanatory examples, necessary documentation, and verification of the declared change stay with it. They are supporting work, not additional product capabilities. Review all supporting material. A new general-purpose validation framework or unrelated structural change needs its own objective and another ticket if over the cap.
- Count changes, not files, commits, ACs, or test cases. Multiple checks can verify one change; the audit is not restricted to one or two files or assertions.
- Every slice remains independently verifiable at published guidance (S1) and/or an actual ChatGPT response (S2). Each response capability includes actual trials after concrete test-plan approval; local simulation does not replace them.
- Preserve established behavior as an invariant. If another independent change proves necessary, revise the breakdown before expanding the ticket.
- No product implementation exists to prefactor. The walking skeleton establishes a minimal direct-use core/YAML path; the route is introduced separately.
- Every declared rule has classification, required propositions, conditions, compatible/conflicting examples, and traceable attribution with evidence limits. These support its capability rather than adding a separate research workflow.
- Each ticket retains observations, failures, reruns, and content revisions under its approved trial policy. The final ticket reuses qualifying evidence and fills missing/affected integration cases, not all testing from scratch.

## Approved slices

### 1. T-0000 — Connect Takahashi core guidance to a YAML handoff

**Blocked by:** None.

**Change objectives (2):**
1. Independently usable, source-attributed Takahashi core guidance.
2. Complementary Markdown and a parseable YAML handoff with the agreed fields.

**What it delivers:** A direct caller receives all mandatory propositions of takahashi.text_primary and a YAML profile containing style_id, core_rules, and adjustable_rules. Rule records have stable English IDs and nonempty constraints; the adjustable list may initially be empty. Preserve relative scale, primary/supporting relationships, and declared conditions. The source record states classification, evidence basis, limits, and compatible/conflicting examples. This is the walking skeleton's real S1/S2 path; use a Taiwan Traditional Chinese happy path. Adjustment handling, JSON, language variants, and route behavior are separate increments. Land the skeleton using the prescribed branch/merge boundary before dependent work.

**Verification:** After concrete test-plan approval, inspect the core/source record, parse YAML, compare Markdown/settings meaning, and retain an actual ChatGPT request, supplied content revision, response, available host/model information, and verdict. No general-purpose testing framework is added.

**Traceability:** TR-02, TR-03, TR-08, TR-09, TR-19–TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33 (core/YAML subset).

### 2. T-0001 — Add independently usable Jobs core guidance

**Blocked by:** T-0000.

**Change objectives (1):**
1. Independently usable, source-attributed Jobs core guidance.

**What it delivers:** A direct caller obtains jobs.single_focus through the existing Markdown/YAML contract. Text/visual elements support one stated display, benefit, reveal, or comparison point. Source records distinguish observations from project synthesis, with conditions and compatible/conflicting examples. Several objects can support one comparison; unrelated primary claims conflict with the core. Do not invent a mandatory whole-deck narrative or creator-backed timing formula.

**Verification:** Source/document review and actual direct-use ChatGPT core trials verify the identifying relationship and existing handoff. This ticket does not add adjustment response handling.

**Traceability:** TR-02, TR-04, TR-08, TR-09, TR-19–TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33 (Jobs core subset).

### 3. T-0002 — Add independently usable Wangxing core guidance

**Blocked by:** T-0000.

**Change objectives (1):**
1. Independently usable, source-attributed 張忘形 core guidance.

**What it delivers:** A direct caller obtains wangxing.text_visual_relation through the existing Markdown/YAML contract. Concise viewpoint text and a meaningful visual relationship communicate the same viewpoint and aid understanding. Source records include classification, conditions, evidence limits, and compatible/conflicting examples. Identify 張忘形, not 王興; humor, monochrome appearance, and oral-only use are not mandatory.

**Verification:** Source/document review and actual direct-use ChatGPT core trials verify identity and the existing handoff. Adjustment response handling remains separate.

**Traceability:** TR-02, TR-05, TR-08, TR-09, TR-19–TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33 (Wangxing core subset).

### 4. T-0003 — Add independently usable Gates core guidance

**Blocked by:** T-0000.

**Change objectives (1):**
1. Independently usable, source-attributed Gates core guidance.

**What it delivers:** A direct caller obtains gates.evidence_relation through the existing Markdown/YAML contract. Evidence, quantities, or system elements relate to a stated comparison/system point; preserve labels, units, assumptions, and qualifications needed to interpret supplied evidence. Source records state project synthesis, conditions, and compatible/conflicting examples, without an official-method or mandatory-density claim.

**Verification:** Source/document review and actual direct-use ChatGPT core trials verify analytical relationships, necessary qualifiers, and the established handoff. Adjustment response handling remains separate.

**Traceability:** TR-02, TR-06, TR-08, TR-09, TR-19–TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33 (Gates core subset).

### 5. T-0004 — Handle Takahashi adjustments and core conflicts

**Blocked by:** T-0000.

**Change objectives (2):**
1. Apply compatible non-core Takahashi adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

**What it delivers:** Accepted non-core changes retain text priority and every applicable core condition in both representations. Explicitly subordinate charts/notes remain compatible. A core-replacing request receives the rule ID, conflicting request, broken proposition, and a retaining suggestion. Keep original core settings; do not apply conflicting overrides or unaccepted alternatives. Attribute every declared adjustable rule.

**Verification:** Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings, including applicable conditions.

**Traceability:** TR-02, TR-08, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33 (Takahashi adjustments).

### 6. T-0005 — Handle Jobs adjustments and core conflicts

**Blocked by:** T-0001.

**Change objectives (2):**
1. Apply compatible non-core Jobs adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

**What it delivers:** Color changes or several objects serving one comparison remain compatible. Unrelated competing primary claims receive the required rule ID, conflicting request, broken proposition, and retaining suggestion. Markdown/settings reflect accepted changes, retain all core propositions/conditions, and exclude unaccepted alternatives. Attribute declared adjustable rules.

**Verification:** Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings.

**Traceability:** TR-02, TR-08, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33 (Jobs adjustments).

### 7. T-0006 — Handle Wangxing adjustments and core conflicts

**Blocked by:** T-0002.

**Change objectives (2):**
1. Apply compatible non-core Wangxing adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

**What it delivers:** Color or omitting humor remains compatible while the meaningful text/visual relationship persists. Replacing it with unrelated decoration receives the required conflict explanation and retaining suggestion. Both representations reflect accepted adjustments and conditions, exclude unaccepted alternatives, and retain the original core. Attribute declared adjustable rules.

**Verification:** Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings.

**Traceability:** TR-02, TR-08, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33 (Wangxing adjustments).

### 8. T-0007 — Handle Gates adjustments and core conflicts

**Blocked by:** T-0003.

**Change objectives (2):**
1. Apply compatible non-core Gates adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

**What it delivers:** Reduced decoration or more whitespace remains compatible while evidence relationships and interpretation-critical qualifiers persist. Removing necessary labels/assumptions receives the required core-conflict explanation and retaining suggestion. Reflect accepted changes consistently, preserve the original core, exclude unaccepted alternatives, and attribute adjustable rules.

**Verification:** Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings and required qualifiers.

**Traceability:** TR-02, TR-08, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33 (Gates adjustments).

### 9. T-0008 — Honor explicit JSON requests with the same rule contract

**Blocked by:** T-0001, T-0002, T-0003.

**Change objectives (1):**
1. JSON serialization selection for existing guidance.

**What it delivers:** Explicit JSON requests change serialization, not fields, types, rule IDs, propositions, or conditions. Otherwise YAML remains the default. Completed guidance emits Markdown and exactly one structured format. Handle the existing record shape, including adjustable records when present, without implementing adjustment behavior here.

**Verification:** Parsing and actual ChatGPT format-selection trials compare the same catalog checklist across YAML/JSON, including a scope-changing condition. Integration covers subsequently added adjustment/routing combinations.

**Traceability:** TR-19–TR-23, TR-28, TR-33 (serialization).

### 10. T-0009 — Preserve user language and stable identifiers

**Blocked by:** T-0001, T-0002, T-0003.

**Change objectives (1):**
1. Consistent requested-language behavior for guidance.

**What it delivers:** Visible explanations and constraint text follow requested/conversation language. Chinese uses Taiwan Traditional Chinese. Field names, style IDs, and catalog rule IDs remain English and stable. Translation preserves propositions/conditions. Apply this to existing response types; later routes inherit the same language invariant rather than adding a divergent rule.

**Verification:** Actual Chinese/English ChatGPT trials and semantic ID/condition checks for existing response types. Final integration checks additional route-response combinations.

**Traceability:** TR-19, TR-20, TR-23, TR-24, TR-26, TR-28, TR-33 (language/identity).

### 11. T-0010 — Honor explicit styles and report inaccessible guidance

**Blocked by:** T-0001, T-0002, T-0003.

**Change objectives (2):**
1. Route an explicit supported choice to that actual style.
2. Report inaccessible selected guidance without fabricating loaded rules.

**What it delivers:** One small route honors a named supported style despite contrary inferred suitability or missing optional context. Read selected guidance/supporting material as needed and preserve direct-use meaning and the existing handoff. Descriptions distinguish selection from named-style use. Inaccessible guidance produces an honest report without local-tool/MCP assumptions. Contextual selection and unresolved-choice clarification remain separate.

**Verification:** Actual explicit-route trials for four styles, direct/routed semantic comparisons, optional missing-context and inaccessible-guidance cases. Check current variants; final integration covers the independently added combinations.

**Traceability:** TR-01, TR-02, TR-10–TR-12, TR-19–TR-26, TR-28, TR-30, TR-32, TR-33 (explicit routing/availability).

### 12. T-0011 — Select from focus anchors or ask for missing purpose

**Blocked by:** T-0010.

**Change objectives (2):**
1. Select one eligible style from supplied purpose/expression anchors.
2. Ask for missing purpose/expression information when no anchor is supplied.

**What it delivers:** Without a style preference, sufficient context produces one eligible style and a reason citing the supplied anchor and selected focus, without optional-field questions. Multiple eligible anchors need no unique winner. Generic/audience-only requests ask for missing purpose/expression need without invented facts/settings. Preserve explicit-choice precedence and established handoff/language invariants.

**Verification:** Actual ChatGPT concept-explanation, evidence-comparison, multiple-anchor, generic-request, and audience-only cases, including the fixed branch examples.

**Traceability:** TR-13, TR-14, TR-24, TR-28, TR-31.

### 13. T-0012 — Clarify unresolved names and multiple styles

**Blocked by:** T-0010.

**Change objectives (2):**
1. Clarify ambiguous or unsupported named styles within the supported set.
2. Clarify unresolved requests for multiple primary styles.

**What it delivers:** Unknown/ambiguous names ask for the intended supported style. Multiple-style or per-page mixing requests ask for one primary style. Do not invent presets, mixing, or a profile before selection. Existing supported choices retain explicit-route behavior and responses follow the shared language rule.

**Verification:** Actual ChatGPT ambiguous/unsupported-name and multiple-style clarification cases, with no fabricated profile.

**Traceability:** TR-15, TR-16, TR-24, TR-28.

### 14. T-0013 — Keep quoted material separate from caller instructions

**Blocked by:** T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0011, T-0012.

**Change objectives (1):**
1. Caller-instruction versus source-material interpretation.

**What it delivers:** Quoted commands do not override caller style, format, language, or adjustment instructions unless explicitly adopted. Material can still supply purpose/audience/expression context. Preserve existing direct/routed behavior while making this boundary explicit across the implemented control dimensions.

**Verification:** Actual ChatGPT conflicting-quote and explicit-adoption cases, including the fixed caller Takahashi/default-YAML request with quoted Gates/JSON commands. All affected controls exist before cross-control trials.

**Traceability:** TR-02, TR-11, TR-13, TR-23, TR-24, TR-28, TR-34.

### 15. T-0014 — Check collection completeness and deliver acceptance evidence

**Blocked by:** T-0013.

**Change objectives (2):**
1. Collection-level guidance/source/contract completeness review.
2. Versioned first-release acceptance evidence handoff.

**What it delivers:** A user can inspect five skills, distinct identities, source limits, scope, discoverability, references, and handoff consistency. Link every AC to applicable document checks and actual ChatGPT observations for the release candidate. Reuse qualifying evidence only for applicable revisions/behaviors; run approved missing/affected cases. Preserve failures/reruns and report pass/fail/unverified honestly. State Skills MCP loading separately; an unverified loading status is permitted by AC-19 and needs no server/connection development.

**Verification:** Final candidate/coverage audit and approved missing/affected actual trials. Successful retries do not erase failures for the same revision. Evidence remains limited to named content revisions and observed host/model surfaces.

**Traceability:** TR-01, TR-07, TR-27–TR-30; collection-level confirmation of every remaining row and AC-01–AC-20.

## Blocking rationale

- T-0000 has no blocker and lands the first real core/YAML path.
- T-0001–T-0003 reuse that seam/contract and do not depend on each other.
- T-0004–T-0007 wait only for their own style core.
- JSON, language, and explicit four-style route tickets T-0008–T-0010 wait for all core styles. They need not wait for every adjustment feature; final integration covers combinations added later.
- T-0011 and T-0012 need the explicit route and do not block each other.
- T-0013 verifies caller/material interpretation across adjustments, serialization, language, and routing controls, so those capabilities must exist first.
- T-0014 waits for T-0013; the remaining prerequisites are transitive.

Each ticket gets its own branch. These edges do not assert concurrent implementation authorization.

## Traceability allocation

Owners implement/verify the behavior; T-0014 checks complete collection coverage and revision applicability. A partial slice does not claim a whole row or AC has passed. The accepted matrix remains unchanged.

| Matrix row | Implementation / evidence owner(s) |
| --- | --- |
| TR-01 | T-0010, T-0014 |
| TR-02 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0010, T-0013 |
| TR-03 | T-0000, T-0004 |
| TR-04 | T-0001, T-0005 |
| TR-05 | T-0002, T-0006 |
| TR-06 | T-0003, T-0007 |
| TR-07 | T-0014 |
| TR-08 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007 |
| TR-09 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009 |
| TR-10 | T-0010 |
| TR-11 | T-0010, T-0013 |
| TR-12 | T-0010 |
| TR-13 | T-0011, T-0013 |
| TR-14 | T-0011, T-0009 |
| TR-15 | T-0012, T-0009 |
| TR-16 | T-0012, T-0009 |
| TR-17 | T-0004, T-0005, T-0006, T-0007 |
| TR-18 | T-0004, T-0005, T-0006, T-0007 |
| TR-19 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0010 |
| TR-20 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0010 |
| TR-21 | T-0000, T-0001, T-0002, T-0003, T-0008, T-0010 |
| TR-22 | T-0008, T-0010 |
| TR-23 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0010, T-0013 |
| TR-24 | T-0009, T-0011, T-0012, T-0013 |
| TR-25 | T-0000, T-0001, T-0002, T-0003, T-0010 |
| TR-26 | T-0000, T-0001, T-0002, T-0003, T-0009, T-0010 |
| TR-27 | T-0014 |
| TR-28 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0010, T-0011, T-0012, T-0013, T-0014 |
| TR-29 | T-0014 |
| TR-30 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0010 |
| TR-31 | T-0011 |
| TR-32 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0010 |
| TR-33 | T-0000, T-0001, T-0002, T-0003, T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0010 |
| TR-34 | T-0013 |

## 使用者審核（zh-TW）

### 粒度修正紀錄

使用者要求確認每張票的反思／稽核是否只涉及一至兩個功能或結構變更。本版採用這個上限，把上一版「完整樣式」拆成核心、調整、格式、語言與 route 行為，共 15 張票，每票明列一至兩個變更目標。來源、例子及驗證跟隨各自的目標，所有受影響的檔案與條件仍須查核；使用者已於 2026-10-03 回覆「都核准」，核准 TB-01、TB-02、TB-03。

舊提案尚未發布，因此重排未變更永久 ID。核准後正式配置 T-0000～T-0014，往後維持這些永久票號。

| 審核編號 | 類別 | 狀態 | 決定 |
| --- | --- | --- | --- |
| TB-01 | 拆票粒度：每票一至兩個可獨立稽核的變更 | 已核准 | 2026-10-03：「都核准」 |
| TB-02 | 依賴關係：是否有漏列或多餘阻擋 | 已核准 | 2026-10-03：「都核准」 |
| TB-03 | 交付與驗收配置：是否完整且符合純風格範圍 | 已核准 | 2026-10-03：「都核准」 |

### TB-01：已核准的拆票粒度

| 編號 | 永久票號 | 變更一 | 變更二 | 白話例子 |
| --- | --- | --- | --- | --- |
| 1 | T-0000 | 高橋流核心指引 | Markdown＋YAML 交接契約 | 先讓真正的 ChatGPT 回傳詞句為主的指引及可解析設定。 |
| 2 | T-0001 | 賈伯斯流核心指引 | — | 所有元素支持同一展示／比較焦點，沿用既有交接格式。 |
| 3 | T-0002 | 忘形流核心指引 | — | 精簡觀點與有意義的視覺關係，沿用既有交接格式。 |
| 4 | T-0003 | 比爾蓋茲流核心指引 | — | 證據／數值／系統連到分析重點，保留必要條件。 |
| 5 | T-0004 | 高橋流相容調整 | 高橋流核心衝突回應 | 輔助圖表可接受；圖表取代詞句主角時說明衝突。 |
| 6 | T-0005 | 賈伯斯流相容調整 | 賈伯斯流核心衝突回應 | 多個物件可支持共同焦點；無關主張互相競爭時說明衝突。 |
| 7 | T-0006 | 忘形流相容調整 | 忘形流核心衝突回應 | 可不用幽默；無關裝飾取代有意義圖文關係時說明衝突。 |
| 8 | T-0007 | 比爾蓋茲流相容調整 | 比爾蓋茲流核心衝突回應 | 可增加留白；刪除必要的單位／假設時說明衝突。 |
| 9 | T-0008 | 指定 JSON 的格式切換 | — | 同一規則改用 JSON，保留欄位、ID 與意思。 |
| 10 | T-0009 | 說明語言與 ID 一致性 | — | 中文用台灣繁體中文，英文可換說法，規則 ID 不變。 |
| 11 | T-0010 | 指定樣式的 route | 無法取得指引的回報 | 指定 Jobs 就載入 Jobs；取不到指引時清楚回報。 |
| 12 | T-0011 | 根據情境選樣式 | 情境不足時澄清 | 介紹 AI 可依概念說明選擇；只說受眾是教師則問用途。 |
| 13 | T-0012 | 名稱不明／不支援的澄清 | 多種主要樣式的澄清 | 找不到名稱或要求混搭時，釐清要用哪一種支援樣式。 |
| 14 | T-0013 | 使用者指令與引用素材的界線 | — | 你指定高橋流，素材中「改用 Gates」不會改掉你的選擇。 |
| 15 | T-0014 | 五個 skills 的整體文件稽核 | 首版驗收證據交付 | 文件完整性與真實試用結果分別呈現，MCP 未測就標明。 |

**使用者決定：** 2026-10-03 回覆「都核准」，明確核准三類工作分解。無須再次逐類提問。

### 發布與下一階段

已依專案 tracker 正式建立 15 張票，一票一檔，英文正文加台灣繁體中文稽核段落，使用 `status: todo` 與 `blocked_by`。各票保留一至兩個變更目標與 traceability。T-0000 位於 round-0 walking-skeleton 群組，其餘位於本 epic 群組。

各票具體 test plan table 在寫測試前另行核准；反思／稽核對照該票明列的一至兩個變更目標，並查核其相關實作、文件與驗證證據。

## Published tickets

| Ticket | File |
| --- | --- |
| T-0000 | [Connect Takahashi core guidance to a YAML handoff](../../.proj.tickets/0000-walking-skeleton/T-0000-walking-skeleton.md) |
| T-0001 | [Add independently usable Jobs core guidance](../../.proj.tickets/0001-style-guidance/T-0001-jobs-core.md) |
| T-0002 | [Add independently usable Wangxing core guidance](../../.proj.tickets/0001-style-guidance/T-0002-wangxing-core.md) |
| T-0003 | [Add independently usable Gates core guidance](../../.proj.tickets/0001-style-guidance/T-0003-gates-core.md) |
| T-0004 | [Handle Takahashi adjustments and core conflicts](../../.proj.tickets/0001-style-guidance/T-0004-takahashi-adjustments.md) |
| T-0005 | [Handle Jobs adjustments and core conflicts](../../.proj.tickets/0001-style-guidance/T-0005-jobs-adjustments.md) |
| T-0006 | [Handle Wangxing adjustments and core conflicts](../../.proj.tickets/0001-style-guidance/T-0006-wangxing-adjustments.md) |
| T-0007 | [Handle Gates adjustments and core conflicts](../../.proj.tickets/0001-style-guidance/T-0007-gates-adjustments.md) |
| T-0008 | [Honor explicit JSON requests with the same rule contract](../../.proj.tickets/0001-style-guidance/T-0008-json-settings.md) |
| T-0009 | [Preserve user language and stable identifiers](../../.proj.tickets/0001-style-guidance/T-0009-language-consistency.md) |
| T-0010 | [Honor explicit styles and report inaccessible guidance](../../.proj.tickets/0001-style-guidance/T-0010-explicit-style-route.md) |
| T-0011 | [Select from focus anchors or ask for missing purpose](../../.proj.tickets/0001-style-guidance/T-0011-context-style-route.md) |
| T-0012 | [Clarify unresolved names and multiple styles](../../.proj.tickets/0001-style-guidance/T-0012-style-choice-clarification.md) |
| T-0013 | [Keep quoted material separate from caller instructions](../../.proj.tickets/0001-style-guidance/T-0013-quoted-material-boundary.md) |
| T-0014 | [Check collection completeness and deliver acceptance evidence](../../.proj.tickets/0001-style-guidance/T-0014-release-evidence.md) |
