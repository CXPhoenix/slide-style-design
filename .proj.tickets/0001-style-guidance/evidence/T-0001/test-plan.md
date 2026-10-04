# T-0001 test plan

Status: approved; user replied A on 2026-10-03, approving TP-01–TP-06, CT-01/CT-02 and execution/retry policy.
Date: 2026-10-03. Branch: `tickets/T-0001/jobs-core`.

Sources: [ticket](../../T-0001-jobs-core.md), [accepted spec](../../../../.proj.specs/0001-style-guidance/spec.en.md), [traceability](../../../../.proj.specs/0001-style-guidance/traceability.md), and [source notes](../../../../docs/research/2026-10-03-takahashi-jobs.md).
Accepted spec/matrix SHA-256 verified against `review/accepted.json` at entry.
T-0000 is done and landed on main; its S1/S2 seams and YAML contract exist.

## Scope

One change objective: independently usable, source-attributed Jobs core guidance.
Reuse the existing handoff; no JSON switch, language expansion, adjustment handler,
route, rewriting, narrative planning, renderer or export is added. This increment's
happy path is Taiwan Traditional Chinese, as in T-0000. The published package is
`skills/jobs-style/`, with concise entry and supporting references as needed.

## Test plan table

| ID | Seam | Test intent / expected behavior | Verification | AC / traceability | Boundary |
| --- | --- | --- | --- | --- | --- |
| TP-01 | S1 published entry | Named Jobs entry with useful description and accessible supporting references; direct use without route or local tools | Bounded Python unittest plus entry review | AC-05, AC-16; TR-09, TR-25, TR-26 | No assumed local filesystem or MCP access by consumers |
| TP-02 | S1 core/source record | `jobs.single_focus`: display, benefit, reveal or comparison elements support one stated focal point; text/visual elements support that point rather than competing unrelated claims | Semantic review against accepted core propositions, source notes and independent Spec review | AC-03, AC-04, AC-20; TR-04, TR-08, TR-30, TR-32 | Several objects can support one comparison. Unrelated equal-primary claims conflict. Distinguish observations from synthesis and disclose reading limits; no mandatory whole-deck sequence or creator-backed timing/word/element-count formula |
| TP-03 | S1 existing handoff | Published example has complementary Markdown and one YAML profile with `style_id: jobs`, `core_rules`, `adjustable_rules`; mandatory fixed ID, unique nonempty English IDs and nonempty constraints, JSON-compatible types | Bounded parse/schema unittest plus semantic review | AC-12–AC-14; TR-19–TR-21, TR-23, TR-33 | Empty adjustable list allowed; both representations retain all core relationships and applicable conditions |
| TP-04 | S2 actual ChatGPT CT-01 | Direct zh-TW guidance with all Jobs core propositions and exactly one YAML profile | One human-operated actual ChatGPT execution; response parsing plus semantic audit | AC-03, AC-05, AC-12–AC-16, AC-18; TR-04, TR-09, TR-19–TR-21, TR-23, TR-25, TR-28 | No route or optional-context prerequisite; no replacement with black-background/theme-only identity |
| TP-05 | S2 actual ChatGPT CT-02 | Four products serve one supplied comparison focus; no single-object ban, unrelated focus invention or removal of interpretation conditions | One separate actual ChatGPT execution; structure plus semantic audit | AC-02, AC-03, AC-12, AC-14, AC-18, AC-20; TR-02, TR-04, TR-19, TR-20, TR-28, TR-30, TR-32, TR-33 | Existing material is context, not an adjustment command. Return style guidance, not revised content, a page plan or a mandatory buildup/reveal/demo/recap itinerary |
| TP-06 | S1/S2 evidence | Retain fixed requests, supplied candidate content and hashes, complete responses, available model/effort/host, per-check verdicts and any failures/retries | Evidence audit | AC-18, AC-19; TR-28 | Missing observations stay unverified; document checks do not prove model behavior; MCP loading separately unverified |

## Fixed actual ChatGPT cases

### CT-01 — Direct Jobs core guidance

> 請使用賈伯斯流，提供適用於現場投影的簡報風格指引與設定。以台灣繁體中文回覆。

Expected: named Jobs identity and `jobs.single_focus` in Markdown; one stated
focal point supported by display/benefit/reveal/comparison elements and text/visual
evidence in both Markdown and constraint, without unrelated competing claims.
Exactly one YAML profile passes the existing contract. No mandatory deck-wide
narrative or fixed numerical formula; direct guidance without optional questions.

### CT-02 — Multiple objects, one comparison point

> 請使用賈伯斯流提供風格指引與設定。用途是現場投影；既有素材有 A、B、C、D 四款產品，共同展示「同一測試條件下的電池續航比較」，且須保留「結果不代表其他使用情境」的限定。請針對這個既定比較焦點提供風格指引。以台灣繁體中文回覆。

The product names and context are invented test material. Expected: all four
objects may support the same comparison; guidance explicitly keeps one focal
point and subordinate/supporting text/visual relationships. Preserve the comparison
condition and non-generalizability in Markdown and constraint. No invented numbers,
single-object mandate, rewritten comparison, page split, file production or speaking
itinerary. This verifies core guidance, not a requested-adjustment response handler.

## Execution and retry policy

Reuse the approved human-operated method: supply complete versioned entry/references
inline in two fresh ChatGPT conversations, one case each. The user operates; the
assistant prepares packets and audits complete returned responses. Use the same
conversation model and medium effort for both; record the visible model label and
leave the exact model identifier unknown if unavailable. Record prepared inputs
separately from independently exported actual submissions, if any.

Each final candidate runs each case once; all necessary checks pass both counted
responses. A semantic/structural failure is retained for its candidate, followed by
skill correction and a new candidate hash; rerun both cases on that new candidate.
An undelivered/technical interruption stays unverified, with at most one technical
retry per case/candidate. A delivered failing answer is not an interruption.
Retain failures and retries; never discard runs until a success appears.

## TDD and completion

After approval: one failing entry check, minimal entry implementation; record the
missing semantic propositions before adding the core/source guidance; then one
failing handoff check followed by its minimal example. Check meaning against the
accepted spec, not word-for-word example matching or keyword-count heuristics.
No general validation framework or new tooling is needed; reuse Python unittest
and installed PyYAML. Keep the existing Takahashi tests unchanged unless evidence
requires a related correction.

Run affected tests per cycle and the full suite once at completion, portable
verifier and scoped diff checks. Produce the coverage table with seam, tests,
measured coverage, AC and uncovered/why. Complete independent Standards/Spec
review, security review, actual ChatGPT trials, skill-generated commits and the
prescribed landing boundary. Scope final claims to this ticket, not the full epic.

## 使用者審核（zh-TW）

本票只新增賈伯斯流核心指引，沿用既有交接格式。TP-01～TP-03 查產品文件與設定；
TP-04～TP-05 由你在兩個新 ChatGPT 對話各執行一次；TP-06 查證據。

A：核准全部計畫與兩個固定案例；B：指定編號修改；C：指定編號補充說明。
