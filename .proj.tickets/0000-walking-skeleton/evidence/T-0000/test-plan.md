# T-0000 test plan

Status: approved; user replied A on 2026-10-03, approving TP-01–TP-06, CT-01/CT-02, and the execution/retry policy.
Date: 2026-10-03.
Branch: `tickets/T-0000/walking-skeleton`.

Sources: [ticket](../../T-0000-walking-skeleton.md),
[accepted specification](../../../../.proj.specs/0001-style-guidance/spec.en.md),
[traceability](../../../../.proj.specs/0001-style-guidance/traceability.md).

## Scope and existing seams

The ticket has exactly two change objectives: independently usable Takahashi core
guidance, and complementary Markdown plus a YAML handoff. Use the existing agreed
S1 published-guidance and S2 actual-ChatGPT-response seams; no API, renderer,
general validation framework, or additional product capability is introduced.

Repository observation: no product skills or test suite yet. Python 3.14.3 and
PyYAML are available on this host. Use Python unittest/PyYAML for bounded structural
checks. These checks do not prove semantic compliance; document/response reviews
use the independent mandatory-core propositions from the accepted spec.

## Proposed test plan table

| ID | Seam | Test intent / expected behavior | Scope | Acceptance criterion / traceability | Boundary conditions |
| --- | --- | --- | --- | --- | --- |
| TP-01 | S1: published skill entry | A consuming agent can identify and use Takahashi guidance directly; name/description are present, and referenced supporting material exists. | Automated package/document checks plus entry-description review. | AC-05, AC-16; TR-09, TR-25, TR-26 | No route prerequisite, shell/local-tool dependency, or assumed MCP connection. |
| TP-02 | S1: core/source record | Declare `takahashi.text_primary`: words/phrases are the primary visual/message carrier, relative scale establishes priority, and included detail is supporting rather than equal/dominant. Record classification, source basis, reading limits, conditions, and compatible/conflicting examples. | Semantic document review against the accepted core record and existing source notes. | AC-03, AC-04, AC-20; TR-03, TR-08, TR-30, TR-32 | Supporting chart/notes are not universally banned; no creator-backed numerical limit or unverified full-book claim. Boundary examples are reference material, not new adjustment response handling. |
| TP-03 | S1: published YAML handoff example | Parseable YAML has `style_id: takahashi`, lists `core_rules` and `adjustable_rules`, all mandatory IDs, unique nonempty English `rule_id` values, and nonempty string `constraint` values. Markdown and constraints retain required propositions/conditions. | Automated parse/schema checks plus semantic example review. | AC-12, AC-13, AC-14; TR-19–TR-21, TR-23, TR-33 | Empty adjustable list is valid. YAML uses JSON-compatible types; no custom tags. Conditions cannot disappear from constraints. |
| TP-04 | S2: actual ChatGPT response | CT-01 delivers directly in Taiwan Traditional Chinese, with the mandatory core meaning in Markdown and exactly one parseable YAML profile using stable IDs. | One actual ChatGPT execution; structural extraction/checks plus semantic response review. | AC-05, AC-12–AC-15, AC-18; TR-09, TR-19–TR-21, TR-23, TR-28 | No JSON request, no route, and no adjustment capability required. The supplied skill content revision is recorded. |
| TP-05 | S2: actual ChatGPT response | CT-02 preserves the conditional supporting-detail relationship in both representations and returns style guidance for existing material. | One separate actual ChatGPT execution; structural and semantic review. | AC-02, AC-03, AC-12, AC-14, AC-18; TR-02, TR-03, TR-19, TR-20, TR-28, TR-33 | It does not rewrite the supplied research statement, split pages, produce a deck, or replace necessary qualifications with a visual shortcut. This tests core guidance and scope, not accepting/rejecting a requested adjustment. |
| TP-06 | S1/S2: retained evidence | Every planned ChatGPT observation has request, supplied skill content/hash, response, available host/model information, and per-check verdict; failures and reruns remain associated with their content revision. | Evidence review; no fabricated behavior results. | AC-18, AC-19; TR-28 | Missing observations remain unverified. MCP product loading is separately unverified. |

## Fixed actual-ChatGPT cases

Supply the entry and all supporting material needed for the mandatory core directly
in a fresh ChatGPT conversation, recording exactly what was supplied. This does not
assume Skills MCP transport or access to repository paths.

The proposed execution method is human-operated ChatGPT: the user pastes the
prepared content and fixed request; the assistant supplies the packet and checks
the returned observations. Model-backed behavior is checked on the actual ChatGPT
surface rather than inferred from Codex or local simulations.

### CT-01 — Direct core guidance and default YAML

Request:

> 請使用高橋流，提供適用於現場投影的簡報風格指引與設定。以台灣繁體中文回覆。

Expected: delivery without route or optional-context questions; `style_id` is
`takahashi`; mandatory ID and all primary-carrier/relative-scale/supporting-detail
propositions appear in Markdown and YAML constraints; required field/type and
uniqueness checks pass; empty `adjustable_rules` is permitted. Exactly one settings
format, YAML, accompanies Markdown.

### CT-02 — Existing material and conditional supporting detail

Request:

> 請使用高橋流提供風格指引與設定。用途是現場投影研究結果；既有素材為「在同一測試環境的 30 位受試者中，完成時間平均縮短 20%；結果不代表其他環境」，另有補充註解。以台灣繁體中文回覆。

The statement is an invented test example, not a factual research finding.

Expected: delivery of guidance/settings, not transformation of the supplied statement;
all core propositions remain, including the conditional supporting role of other
detail, in both Markdown and YAML. No unconditional demand to remove required
qualifications, chart/notes ban, rewritten study claim, page plan, or export is
returned as the skill's deliverable. Existing material provides context rather than
a request to implement an adjustment. Schema/ID/format checks also pass.

## Execution and retry policy

- The final-content candidate runs CT-01 and CT-02 once each in separate fresh
  ChatGPT conversations; every required check must pass in both counted executions.
- A semantic or structural failure is a failure for that content revision. Correct
  the skill and record a new revision; do not rerun until success while discarding
  earlier failures. Re-execute both cases for the corrected final candidate.
- An interrupted/undelivered run remains recorded as unverified; one technical
  retry is permitted for that case and revision. Record the interruption and retry.
  An actual response that fails a check is not an interruption.
- Before each candidate run, record supplied content/hash and expected propositions.
  Preserve complete requests and responses, observed host/model labels when
  available, and verdicts; unknown host/model fields remain unknown.
- Document checks, actual ChatGPT trials, and MCP loading have separate verdicts.
  Do not claim general reliability beyond these recorded executions.

## TDD and completion

After approval, write only one failing check at the current seam, implement the
minimum to pass it, then proceed to the next behavior. For semantic document checks,
record the missing/violated accepted proposition before adding the corresponding
guidance. Automated checks are not proxies for that semantic review.

At completion run affected checks and the full product test suite once, plus the
portable project verifier and diff checks. Record the required coverage report,
including unmeasured semantic/model coverage. Complete change review, security
review, actual-surface verification, and ticket landing according to the workflow.

## 使用者審核（zh-TW）

本計畫只驗證 T-0000 的兩個變更：高橋流核心指引、Markdown＋YAML 交接契約。
TP-01～TP-03 查文件；TP-04～TP-05 在真正的 ChatGPT 各執行一次；TP-06 查驗證據。
實際 ChatGPT 採你操作、我提供可貼上的內容與問題，再稽核回應的方式。

**選項：** A 核准 TP-01～TP-06、CT-01／CT-02 與執行／重試方式；B 指出編號要求修改；C 指出編號要求補充說明。
使用者於 2026-10-03 回覆 A，核准本計畫及執行方式。核准後依 TDD 逐項實作；實際執行結果另記，不從本次核准推論通過。
