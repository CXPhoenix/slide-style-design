# T-0003 test plan

Status: approved; user replied A on 2026-10-04, approving TP-01–TP-06, both fixed cases and execution/retry policy.
Date: 2026-10-04. Branch: `tickets/T-0003/gates-core`.

Sources: [ticket](../../T-0003-gates-core.md), [accepted spec](../../../../.proj.specs/0001-style-guidance/spec.en.md), [traceability](../../../../.proj.specs/0001-style-guidance/traceability.md), [source notes](../../../../docs/research/2026-10-03-wangxing-gates.md).
Frozen spec/matrix hashes match the accepted record; T-0000 is done and landed.
S1 published-guidance and S2 actual-ChatGPT-response seams and existing YAML contract
are reused. Existing Takahashi, Jobs and Wangxing tests remain unchanged.

## Scope

One change objective: independently usable, source-attributed Gates core guidance.
Product package `skills/gates-style/`. The analytical orientation has source support;
`gates.evidence_relation` is project synthesis, not an official creator method.
No mandatory high density, one-page full argument, fixed metrics or universal
no-story/no-humor rule. Taiwan Traditional Chinese happy path and existing
Markdown/YAML contract; no JSON switch, language expansion, route, adjustment
handler, rewriting, analytical calculation, renderer or export.

## Test plan table

| ID | Seam | Expected behavior | Verification | AC / traceability | Boundary |
| --- | --- | --- | --- | --- | --- |
| TP-01 | S1 entry | Named Gates entry, meaningful description, accessible support, independent direct use | Bounded unittest plus entry review | AC-05, AC-16; TR-09, TR-25, TR-26 | No route/local-tool/MCP prerequisite |
| TP-02 | S1 core/source | `gates.evidence_relation` relates evidence/quantities/system elements to a stated comparison/system point; preserve necessary labels, units, assumptions and qualifications | Semantic review against accepted spec/source notes and independent Spec review | AC-03, AC-04, AC-20; TR-06, TR-08, TR-30, TR-32 | Conditional qualifiers when necessary; source classification/limits; compatible whitespace and conflicting removed-label/disconnected-number examples. No official-method/mandatory-density claim or speaker misattribution |
| TP-03 | S1 handoff | Markdown and one YAML preserve core and all applicable qualifiers; `style_id: gates`, agreed lists, mandatory ID, unique nonempty English IDs and nonempty constraints | Bounded schema/type/ID parsing plus semantic review | AC-12–AC-14; TR-19–TR-21, TR-23, TR-33 | Empty adjustable list allowed; JSON-compatible types, no custom tags; no shortening away interpretation conditions |
| TP-04 | S2 CT-01 | Direct zh-TW analytical guidance with fixed core, explicit comparison/system relationship, exactly one valid YAML | One user-operated actual ChatGPT run, structure and meaning audit | AC-03, AC-05, AC-12–AC-16, AC-18; TR-06, TR-09, TR-19–TR-21, TR-23, TR-25, TR-28 | Do not replace relationship with generic high-density/theme instructions or mandatory charts; distinguish project synthesis |
| TP-05 | S2 CT-02 | Existing sparse comparison connects A/B quantities to the stated point and retains metric/units/shared conditions/repeats/qualification in both representations | One separate actual ChatGPT run, structural and semantic audit | AC-02, AC-03, AC-04, AC-12, AC-14, AC-18, AC-20; TR-02, TR-06, TR-19, TR-20, TR-28, TR-30, TR-32, TR-33 | No density mandate, deleted labels, invented benchmark/generalization, calculation/rewrite/page plan/file creation; supplied sparse appearance is context, not adjustment request |
| TP-06 | S1/S2 evidence | Retain request, supplied content/hash, full response, available host/model/effort, verdict and failures/retries | Evidence audit | AC-18, AC-19; TR-28 | Unavailable exact model unknown; actual ChatGPT distinct from local checks/MCP |

## Fixed actual ChatGPT cases

### CT-01 — Direct analytical core

> 請使用比爾蓋茲流，提供適用於現場投影的簡報風格指引與設定。以台灣繁體中文回覆。

Expected: direct delivery with Bill Gates identity and `gates.evidence_relation`;
evidence/quantity/system elements relate to a stated comparison or system point,
necessary interpretation qualifiers retained in Markdown and constraint. One valid
YAML. Project synthesis disclosed without creator-official or mandatory-density claim.
No optional-context prerequisite, production or calculation needed.

### CT-02 — Sparse comparison with required interpretation conditions

> 請使用比爾蓋茲流提供風格指引與設定。用途是現場投影，既有版面有大量留白；分析重點為「兩個方案的平均回應時間比較」。素材是方案 A：120 ms、方案 B：90 ms，兩者使用相同硬體與工作負載，各重複測試 10 次取平均；結果僅適用於此次測試條件。請只針對證據與比較重點的表達關係提供風格指引，保留必要標籤、單位、條件與限定。以台灣繁體中文回覆。

Invented test material, not a real benchmark. Expected: connect labeled A/B average
response times (ms) to the stated comparison; preserve shared hardware/workload,
10-repeat average context and test-specific limitation in Markdown and constraint.
Whitespace is compatible, not grounds for forcing density. No invented values,
new derived performance claim/calculation, rewritten results, page plan or deck.
This tests core guidance for existing material, not accepting/rejecting an adjustment.

## Execution and retry policy

User operates actual ChatGPT: two fresh conversation chats, full versioned skill
entry and needed references inline, one case each. Same default model / medium;
record actual visible labels, leave exact model ID unknown if unavailable. Return
complete responses for assistant audit. Keep prepared inputs separate from any
independently exported submitted inputs.

Each final candidate executes both cases once, all required checks pass both.
Retain a structural/semantic failure, correct skill and make a new content hash;
rerun both cases on that new candidate. A technical interruption/undelivered run
is unverified; at most one technical retry per case/candidate, still recorded.
Delivered incorrect answers are failures, not interruptions. Retain failures/reruns.

## TDD and completion

After approval: one failing entry check, minimal entry; record missing independent
semantic propositions before adding core/source guidance; then one failing handoff
check and its minimal example. No exact-prose/keyword-count semantic oracle.
Reuse unittest/PyYAML without general framework/new tooling. Run affected checks
per cycle and full suite once at completion, portable verifier and scoped whitespace
checks. Coverage table has seam, tests, measured coverage, AC and uncovered/why.
Complete independent Standards/Spec review, security review, actual ChatGPT trials,
skill-generated commits and prescribed landing. This is T-0003 acceptance, not full
epic completion or MCP compatibility.

## 使用者審核（zh-TW）

只新增比爾蓋茲流核心，沿用既有契約。TP-01～TP-03 查文件／設定，TP-04～TP-05
由你在兩個新 ChatGPT 對話各執行一次，TP-06 查證據。不要求計算或製作簡報。

A：核准全部計畫與兩個案例；B：指定編號修改；C：指定編號補充說明。
