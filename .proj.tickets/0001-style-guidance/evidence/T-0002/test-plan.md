# T-0002 test plan

Status: approved; user replied A on 2026-10-04, approving TP-01–TP-06, both fixed cases and execution/retry policy.
Date: 2026-10-04. Branch: `tickets/T-0002/wangxing-core`.

Sources: [ticket](../../T-0002-wangxing-core.md), [accepted specification](../../../../.proj.specs/0001-style-guidance/spec.en.md), [traceability](../../../../.proj.specs/0001-style-guidance/traceability.md), [source notes](../../../../docs/research/2026-10-03-wangxing-gates.md).
Spec and matrix SHA-256 match the accepted frozen record. T-0000 is done; existing
S1/S2 seams and Markdown/YAML contract are reused. T-0001 is also done.

## Scope

One change objective: independently usable, source-attributed 張忘形 core guidance.
Product package: `skills/wangxing-style/`. `wangxing` is a project identifier, not a
claim about the creator's official English name; the creator is 張忘形, not 王興.
Reuse the Taiwan Traditional Chinese happy path and existing contract. No renderer,
content rewriting, JSON switch, language expansion, route, adjustment handler or
whole-deck narrative is added. Humor, monochrome appearance and oral-only use are
not identity requirements.

## Test plan table

| ID | Seam | Expected behavior | Verification | AC / traceability | Boundary |
| --- | --- | --- | --- | --- | --- |
| TP-01 | S1 entry | Named direct-use Wangxing entry identifies 張忘形; description and referenced support exist | Bounded unittest plus identity/description review | AC-05, AC-16; TR-09, TR-25, TR-26 | No route, local tools or MCP prerequisite |
| TP-02 | S1 core/source | `wangxing.text_visual_relation`: concise viewpoint text and visual representation communicate the same viewpoint or an explicitly named relationship; visual aids understanding rather than unrelated decoration | Semantic document and independent Spec review | AC-03, AC-04, AC-20; TR-05, TR-08, TR-30, TR-32 | Source classification, conditions, reading limits, compatible color/no-humor and conflicting unrelated-decoration examples; no mandatory memes/monochrome/oral-only definition, numerical formula or unverified paid-course/full-book claim |
| TP-03 | S1 handoff | Markdown and one YAML agree on all core relationships/conditions; `style_id: wangxing`, fixed mandatory ID, agreed lists and unique nonempty English IDs/nonempty constraints | Bounded YAML schema/type/ID check plus semantic review | AC-12–AC-14; TR-19–TR-21, TR-23, TR-33 | Empty adjustable list allowed; JSON-compatible types, no custom tags; no condition removed for brevity |
| TP-04 | S2 CT-01 | Direct zh-TW guidance identifies creator and core; exactly one valid YAML, meaningful text/visual relationship in both representations | One actual human-operated ChatGPT run; structure and meaning audit | AC-03, AC-05, AC-12–AC-16, AC-18; TR-05, TR-09, TR-19–TR-21, TR-23, TR-25, TR-28 | No theme-only substitute, route prerequisite or mandatory joke |
| TP-05 | S2 CT-02 | Existing color/non-humorous independently read material retains a meaningful viewpoint/visual relationship and necessary restriction | One separate actual ChatGPT run; structural and semantic audit | AC-02, AC-03, AC-04, AC-12, AC-14, AC-18, AC-20; TR-02, TR-05, TR-19, TR-20, TR-28, TR-30, TR-32, TR-33 | No forced black/white, meme or speaker-only use; no rewritten viewpoint, new illustration, page plan or transformation. Context is not an adjustment request |
| TP-06 | S1/S2 evidence | Retain requests, supplied content hashes, complete responses, available model/effort/host, verdicts and failures/retries | Evidence audit | AC-18, AC-19; TR-28 | Missing observations unknown/unverified; actual ChatGPT and MCP distinct |

## Fixed actual ChatGPT cases

### CT-01 — Direct core guidance

> 請使用忘形流（張忘形），提供適用於現場投影的簡報風格指引與設定。以台灣繁體中文回覆。

Expected: creator identity, fixed `wangxing.text_visual_relation`, concise viewpoint
text and meaningful visual representation support the same point or a named
relationship, not decoration alone; Markdown and YAML retain the same meaning and
conditions. One valid YAML profile; direct guidance without route or optional-context
questions. No compulsory jokes or creator-backed numerical limits.

### CT-02 — Color, no humor, independent reading

> 請使用忘形流（張忘形）提供風格指引與設定。既有素材是供讀者自行閱讀的彩色社群圖文，不使用幽默；觀點為「在這個團隊中，清楚說明分工，有助減少重複工作」，既有圖像以相連的任務區塊對應各人的分工。請只針對文字與圖像的表達關係提供風格指引，保留「在這個團隊中」的限定。以台灣繁體中文回覆。

This is invented test material, not a measured research result. Expected: color,
no humor and independent reading are compatible contexts when the core remains.
Guidance explicitly ties concise viewpoint text to the task/person visual relation
and its contribution to understanding; preserve team-specific qualification in both
representations. No universal benefit extrapolation, mandated black/white or meme,
oral-only restriction, new wording/image production/page plan. Existing material
is context rather than a command to implement an adjustment.

## Execution and retry policy

Reuse the user-operated actual ChatGPT method: provide complete versioned entry and
needed supporting references inline, two fresh conversations, one case each. Use
the same default conversation model and medium effort; record actual available
labels and leave exact model identity unknown if unavailable. User supplies complete
responses; assistant checks structure and semantics. Record prepared inputs
separately from independently exported actual submissions, if supplied.

Each final candidate runs each case once; all required checks pass both responses.
Retain structural/semantic failures, correct skill, record a new content hash and
rerun both cases. Undelivered/technical interruption is unverified and permits at
most one technical retry per case/candidate; a delivered failing response is not
an interruption. Preserve all reported failures and retries.

## TDD and completion

After approval, one failing entry check, minimal entry; record missing accepted
semantic propositions before adding core/source guidance; then one failing handoff
check and its minimal example. Exact prose/keyword counts are not semantic oracles.
Reuse unittest/PyYAML; no general framework or new tooling. Preserve existing
Takahashi/Jobs tests. Run affected checks per cycle and full suite once at completion,
portable verifier and scoped whitespace checks. Coverage table lists seams, tests,
measured coverage, AC and uncovered/why. Complete independent Standards/Spec and
security review, actual-surface trials, skill-generated commits and prescribed
landing. Do not claim full epic or MCP acceptance from this ticket.

## 使用者審核（zh-TW）

只新增忘形流核心指引，沿用既有契約。TP-01～TP-03 查文件／設定，TP-04～TP-05
由你在兩個新 ChatGPT 對話各執行一次，TP-06 查證據。不是要求製作圖像或簡報。

A：核准全部計畫與兩個案例；B：指定編號修改；C：指定編號補充說明。
