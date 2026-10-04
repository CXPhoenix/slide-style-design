# Proposed ticket breakdown — style guidance

Historical proposal: superseded by [revision 2](ticket-breakdown.md) after the user's one-to-two-change granularity clarification. Retained for context; this version is not awaiting approval or ticket publication.

Status: proposed; awaiting user approval of granularity, blocking edges, and deliverables.
Created: 2026-10-03.

Sources: [accepted specification](spec.en.md), [traceability](traceability.md),
[completed user specification review](user-review.md), and
[technical review acceptance](review/accepted.json).
The accepted English specification SHA-256 is
`e9aa76437e72a36ca4ed1832e2d856bc48bc7a2ea8aad0ac63112c721d2acef1`.

This is a review proposal, not published tickets or an approved test plan. The
suggested ticket IDs below are provisional; scan the entire local tracker again
before allocating permanent IDs. No existing ticket files were found when drafting.

## Slicing rationale

There are no product skills yet. Following the project's accepted walking-skeleton
ADR, first connect published product guidance (S1) to an actual ChatGPT response
(S2) with a minimal Takahashi skill and a narrow route. This demonstrates a real
guidance/settings path and establishes the means of capturing trial evidence.
It does not establish first-release acceptance or require an MCP connection.

Then complete one independently usable style per ticket. Each style slice includes
source attribution, core and adjustable guidance, applicability conditions,
compatible/conflicting examples, Markdown plus YAML/JSON settings, requested
language behavior, document checks, and actual direct-use ChatGPT trials. Validation
is part of each slice, not postponed wholesale until integration.

Complete the route only when the four finished styles can be accessed. Finish with
collection-level checks and an evidence handoff for the actual release candidate.
The final slice reuses qualifying earlier observations for unchanged content;
changed content, missing cases, or unresolved concerns require appropriate new
checks. It does not substitute summaries for the observations themselves.

The scope is guidance and constraints. No ticket adds rewriting, slide production,
export, automatic mixing, an MCP server, or a universal model-compatibility promise.
No prefactoring is needed: there is no product implementation to refactor.

## Numbered proposal

### 1. T-0000 — Connect a minimal guidance path in ChatGPT

**Blocked by:** None.

**Context:** Round 0 establishes real S1/S2 seams before the first product epic.
Use the already accepted style responsibilities to keep this narrow increment
consistent with the intended product.

**What it delivers:** A caller can directly use minimal source-attributed Takahashi
guidance, or reach the same guidance through an explicit Takahashi route request,
and receive Markdown plus parseable YAML in an actual ChatGPT trial. The fixed
`takahashi.text_primary` record preserves all mandatory propositions. An accessible
guidance package, document/configuration check method, and recorded request,
supplied content revision, response, available host/model information, and verdict
make the path reproducible and inspectable.

**Boundaries:** This increment may use a Taiwan Traditional Chinese happy path;
full JSON/language variants, all adjustments, all four styles, and full selection
are delivered by later tickets. The narrow route reports the availability limit
for unavailable styles rather than silently substituting or inventing guidance.
No first-release compliance claim is made.

**Verification:** Approve the concrete test plan before writing tests or running
the planned trials. Check the mandatory relationship and YAML contract; record
actual direct and explicit-route ChatGPT observations. Local simulation does not
close the ChatGPT seam. Review and land the skeleton before dependent tickets start.

**Requirement contribution:** A bounded subset of TR-02, TR-03, TR-09, TR-10,
TR-19–TR-21, TR-25, TR-26, and TR-28. Full AC closure remains with the epic tickets.

**Publication:** The round-0 ticket belongs to the walking-skeleton tracker group;
it is not a new implementation spec. Retain the prescribed skeleton branch and
merge boundary. The accepted first-release spec is not weakened by this exemption.

### 2. T-0001 — Complete independently usable Takahashi guidance

**Blocked by:** T-0000.

**What it delivers:** A caller obtains complete text-led Takahashi guidance without
the route, with source-qualified rules, applicability conditions, and the fixed
`takahashi.text_primary` core. Supporting charts/notes remain compatible when their
subordinate relationship is explicit. A request replacing the text's primary role
receives the rule ID, conflicting request, broken proposition, and a compatible
suggestion; delivered settings retain the core and omit unaccepted alternatives.
Markdown, default YAML, explicitly requested JSON, and Chinese/English responses
preserve the same rule meaning and conditions.

**Verification:** Source/document and parseability checks plus approved actual
ChatGPT direct-use trials cover identity, compatible adjustment, conflict, the
shared contract, language/format variants, and applicable condition retention.
Preserve all failures, revisions, and reruns under the approved trial policy.

**Traceability:** TR-02, TR-03, TR-08, TR-09, TR-17–TR-26, TR-28, TR-30,
TR-32–TR-34, scoped to this style.

### 3. T-0002 — Complete independently usable Steve Jobs guidance

**Blocked by:** T-0000.

**What it delivers:** A caller obtains complete Jobs guidance without the route.
The fixed `jobs.single_focus` record retains one stated display, benefit, reveal,
or comparison point and the supporting text/visual relationship. Multiple objects
may serve a shared comparison; unrelated competing primary claims produce a core
conflict explanation. Source records distinguish observations from project
synthesis, without a mandatory whole-deck narrative or unsupported timing rules.
The same shared output, adjustment, condition, and language requirements apply.

**Verification:** Source/document checks and approved actual ChatGPT direct-use
trials establish Jobs identity, the declared compatible/conflicting branches, and
the shared handoff contract. This ticket does not depend on completed Takahashi
behavior; it uses the seams and evidence method established by the skeleton.

**Traceability:** TR-02, TR-04, TR-08, TR-09, TR-17–TR-26, TR-28, TR-30,
TR-32–TR-34, scoped to this style.

### 4. T-0003 — Complete independently usable Wangxing guidance

**Blocked by:** T-0000.

**What it delivers:** A caller obtains complete guidance for 張忘形 without the route.
The fixed `wangxing.text_visual_relation` record retains concise viewpoint text
and a meaningful visual relationship supporting the same viewpoint. Color or
omitting humor remains compatible; unrelated decoration replacing that relationship
produces a core conflict explanation. Source-qualified guidance distinguishes the
creator from 王興 and avoids mandatory memes, black-and-white appearance, or oral-only
usage. The shared handoff, adjustment, condition, and language requirements apply.

**Verification:** Source/document checks and approved actual ChatGPT direct-use
trials establish the intended identity, compatible/conflicting branches, and the
shared contract. It does not depend on another completed style.

**Traceability:** TR-02, TR-05, TR-08, TR-09, TR-17–TR-26, TR-28, TR-30,
TR-32–TR-34, scoped to this style.

### 5. T-0004 — Complete independently usable Bill Gates guidance

**Blocked by:** T-0000.

**What it delivers:** A caller obtains complete analytical Gates guidance without
the route. The fixed `gates.evidence_relation` record connects supplied evidence,
quantities, or system elements to a stated comparison/system point and retains
interpretation-critical labels, units, assumptions, and qualifications. Reduced
decoration or more whitespace remains compatible; removing necessary conditions
produces a core conflict explanation. Label the method as source-led project
synthesis, without requiring high density or claiming an official Gates method.
The shared handoff, adjustment, condition, and language requirements apply.

**Verification:** Source/document checks and approved actual ChatGPT direct-use
trials establish analytical identity, necessary qualifiers, compatible/conflicting
branches, and the shared contract. It does not depend on another completed style.

**Traceability:** TR-02, TR-06, TR-08, TR-09, TR-17–TR-26, TR-28, TR-30,
TR-32–TR-34, scoped to this style.

### 6. T-0005 — Route requests to one of the four complete styles

**Blocked by:** T-0001, T-0002, T-0003, T-0004.

**What it delivers:** A caller uses one small route to reach the actual selected
style. Explicit supported choices win over inferred suitability and missing
optional context. Otherwise, a supplied purpose/expression anchor selects one
eligible style with a concise reason. Missing anchors, ambiguous/unsupported names,
and unresolved multi-style requests receive the required clarification. Quoted
material cannot override caller instructions unless explicitly adopted. Routed
guidance preserves the selected style's direct-use identity, core, adjustments,
conditions, identifiers, output format, and requested language. Inaccessible
guidance produces an honest availability report.

**Verification:** Approved actual ChatGPT trials exercise explicit choices for all
four styles, direct/routed semantic comparisons, sufficient/insufficient context,
the fixed branch examples, multiple eligible anchors, multiple/unsupported choices,
quoted commands, and unavailable guidance. Verify core/adjustment preservation and
format/language behavior on the relevant routed cases without inventing a second
style-rule catalog.

**Traceability:** TR-01, TR-02, TR-10–TR-26, TR-28, TR-30–TR-34, scoped to the route.

### 7. T-0006 — Deliver collection-level acceptance and release evidence

**Blocked by:** T-0005.

**What it delivers:** A user can inspect the five-skill release candidate, understand
independent and routed use, and determine first-release readiness from a versioned
evidence record. Check the collection's four identities, source distinctions,
references, scope, descriptions, and handoff consistency. Map every acceptance
criterion to document evidence and actual ChatGPT observations for the applicable
revision, reporting pass/fail/unverified truthfully. Separately state Skills MCP
loading compatibility as unverified unless an actual product loading trial exists;
this ticket does not require developing a server or establishing a connection.

**Verification:** Aggregate qualifying per-ticket evidence, check the actual release
candidate and all 20 criteria, and execute approved missing or affected integration
cases. A failed observation cannot be erased by retry; unexecuted checks cannot pass.
Release evidence is limited to the named revisions and observed host/model surfaces.
The report does not generalize observed results to all future GPT variants.

**Traceability:** TR-01, TR-02, TR-07, TR-08, TR-27–TR-30, plus collection-level
confirmation of the owner evidence for every other traceability row.

## Blocking rationale

- T-0000 has no blockers: it creates the first actual guidance/response path.
- T-0001–T-0004 each wait for the landed skeleton and use its real seams, contract
  baseline, and evidence method. They do not wait for each other.
- T-0005 waits for all four complete styles because its promised behavior is routing
  to any supported style and preserving the actual rule catalog.
- T-0006 waits for T-0005. T-0001–T-0004 are already transitive dependencies, so no
  redundant blocking edges are added.

These are work dependencies, not a claim of parallel implementation authorization.
Each ticket will have its own branch; any future concurrent writers need isolated
checkouts according to the project instructions.

## Traceability allocation

Owners below establish the behavior; T-0006 checks collection completeness and
applicable evidence for every row. T-0000 contributes a subset without closing a
first-release criterion. This allocation does not modify the frozen matrix.

| Matrix row | Implementation / evidence owner(s) |
| --- | --- |
| TR-01 | T-0005, T-0006 |
| TR-02 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-03 | T-0001 |
| TR-04 | T-0002 |
| TR-05 | T-0003 |
| TR-06 | T-0004 |
| TR-07 | T-0006 |
| TR-08 | T-0001, T-0002, T-0003, T-0004 |
| TR-09 | T-0001, T-0002, T-0003, T-0004 |
| TR-10 | T-0005 |
| TR-11 | T-0005 |
| TR-12 | T-0005 |
| TR-13 | T-0005 |
| TR-14 | T-0005 |
| TR-15 | T-0005 |
| TR-16 | T-0005 |
| TR-17 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-18 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-19 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-20 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-21 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-22 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-23 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-24 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-25 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-26 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-27 | T-0006 |
| TR-28 | T-0001, T-0002, T-0003, T-0004, T-0005, T-0006 |
| TR-29 | T-0006 |
| TR-30 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-31 | T-0005 |
| TR-32 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-33 | T-0001, T-0002, T-0003, T-0004, T-0005 |
| TR-34 | T-0001, T-0002, T-0003, T-0004, T-0005 |

## 使用者審核（zh-TW）

沿用先前的表格、成人情境解釋與文字選擇題，一次核准一類。
票號為預計編號，正式發布時才配置永久 IDs。

| 審核編號 | 類別 | 狀態 | 決定 |
| --- | --- | --- | --- |
| TB-01 | 拆票粒度：是否合併或拆細 | 待審核 | |
| TB-02 | 依賴關係：是否有漏列或多餘阻擋 | 待審核 | |
| TB-03 | 交付與驗收配置：是否完整且符合純風格範圍 | 待審核 | |

### TB-01：拆票粒度

| 編號 | 預計票號 | 標題 | 完成後能驗證什麼（白話例子） | Blocked by |
| --- | --- | --- | --- | --- |
| 1 | T-0000 | 最小 ChatGPT 使用路徑 | 先做薄版高橋流與指定高橋流的 route，實際取得 Markdown＋YAML 並留下試用紀錄；像先把一條線接通。 | 無 |
| 2 | T-0001 | 完整高橋流樣式 skill | 可獨立取得以詞句為主角的完整指引，判斷輔助圖表與核心衝突，並驗證實際 ChatGPT 回應。 | T-0000 |
| 3 | T-0002 | 完整賈伯斯流樣式 skill | 可獨立取得圍繞同一展示／效益／比較焦點的指引，判斷相容調整與競爭主張，並驗證實際回應。 | T-0000 |
| 4 | T-0003 | 完整忘形流樣式 skill | 可獨立取得精簡觀點與有意義圖文關係的指引，判斷相容調整與無關裝飾，並驗證實際回應。 | T-0000 |
| 5 | T-0004 | 完整比爾蓋茲流樣式 skill | 可獨立取得證據／數值／系統關係的指引，保留理解所需條件，判斷調整與衝突，並驗證實際回應。 | T-0000 |
| 6 | T-0005 | 完整 route skill | 支援四種樣式的指定、情境選擇、必要澄清與無法載入的回報，且保留原樣式規則；像接待人員能正確轉介到四本手冊。 | T-0001～T-0004 |
| 7 | T-0006 | 首版整體驗收與證據交付 | 使用者能檢視五個 skills 的完整性與全部 AC 證據，分清楚文件檢查、ChatGPT 試用與 MCP 載入狀態。 | T-0005 |

四張完整樣式票各自包含來源／規則紀錄、核心與可調指引、條件與例外、Markdown＋YAML／JSON、中英文、文件檢查及實際 ChatGPT 試用。T-0000 只建立最小路徑，不宣稱首版完成。T-0006 彙整適用證據並補足缺漏或受變更影響的驗證。

**目前選擇題：** A 核准七張票的粒度；B 太粗，指出要拆細的票號；C 太細，指出要合併的票號。此題只核准 TB-01；TB-02、TB-03 接著分別審核。

### 發布與下一階段

全部三類核准後，依專案 tracker 寫成一票一檔，英文正文加台灣繁體中文稽核段落，使用 `status: todo` 與 `blocked_by`。T-0000 放在 round-0 walking-skeleton 群組，其餘放在本 epic 群組；不使用上游範例的 `.scratch/` 或 `ready-for-agent` 狀態。

各票的具體 test plan table 仍須在寫測試前另行核准。本次工作分解核准後建立正式 tickets，接著依專案 pipeline 進入實作階段。
