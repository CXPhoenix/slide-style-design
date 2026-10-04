---
id: T-0000
title: "Connect Takahashi core guidance to a YAML handoff"
epic: 0000-walking-skeleton
status: done
blocked_by: []
---

# T-0000: Connect Takahashi core guidance to a YAML handoff

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence. This is round 0 under [ADR-0001](../../docs/adr/0001-walking-skeleton-then-epic-loop.md): it establishes real seams and does not claim first-release acceptance. The existing first-release spec informs scope without creating a new skeleton spec.

## Deliverable

A direct caller receives all mandatory propositions of takahashi.text_primary and a YAML profile containing style_id, core_rules, and adjustable_rules. Rule records have stable English IDs and nonempty constraints; the adjustable list may initially be empty. Preserve relative scale, primary/supporting relationships, and declared conditions. The source record states classification, evidence basis, limits, and compatible/conflicting examples. This is the walking skeleton's real S1/S2 path; use a Taiwan Traditional Chinese happy path. Adjustment handling, JSON, language variants, and route behavior are separate increments. Land the skeleton using the prescribed branch/merge boundary before dependent work.

## Change objectives

1. Independently usable, source-attributed Takahashi core guidance.
2. Complementary Markdown and a parseable YAML handoff with the agreed fields.

## Acceptance criteria

Traceability contributions: TR-02, TR-03, TR-08, TR-09, TR-19, TR-20, TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Published Takahashi guidance contains takahashi.text_primary and all mandatory primary-carrier, relative-scale, and subordinate-detail propositions; source classification, basis, limitations, conditions, and boundary examples are explicit.
- [x] Actual direct-use guidance contains complementary Markdown and exactly one parseable YAML profile with the agreed fields, stable unique IDs, nonempty constraints, and retained propositions/conditions. An empty adjustable_rules list is valid at this increment.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

After concrete test-plan approval, inspect the core/source record, parse YAML, compare Markdown/settings meaning, and retain an actual ChatGPT request, supplied content revision, response, available host/model information, and verdict. No general-purpose testing framework is added.

The concrete test plan table must be approved before tests are written. The linked test plan is approved; execution evidence and incomplete gates are recorded separately. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 高橋流核心指引。
2. Markdown＋YAML 交接契約。

先讓真正的 ChatGPT 回傳詞句為主的指引及可解析設定。

必須先完成：無。兩項變更已完成，本機檢查與兩個實際 ChatGPT 案例通過，並以 no-ff 合併至本機 main。Skills MCP 載入仍未驗證。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-03 — User explicitly invoked `$implement T-0000`. Branch: `tickets/T-0000/walking-skeleton`. The [proposed test plan](evidence/T-0000/test-plan.md) awaits approval before tests or product implementation are written. The existing uncommitted discovery/spec/ticket artifacts remain preserved.

2026-10-03 — User replied A, approving the [test plan](evidence/T-0000/test-plan.md), fixed ChatGPT cases, and execution/retry method. Proceed with one failing check and one minimal implementation per cycle. Actual ChatGPT observations remain unverified until supplied and audited.

2026-10-03 — Implemented the two scoped document changes with three recorded red/green cycles. Local product suite (two tests), portable verifier and diff check passed. See [coverage](evidence/T-0000/coverage.md), [change review](evidence/T-0000/change-review.md), [security review](../../docs/reviews/security-T-0000.md), and [prepared ChatGPT trials](evidence/T-0000/chatgpt-trials.md). Actual CT-01/CT-02 responses remain unverified; status stays processing and landing is pending.

2026-10-03 — User supplied both complete ChatGPT responses and reported default conversation model / medium effort. Both fixed cases passed structural and semantic checks; see [trial results](evidence/T-0000/trial-results.md). Exact model ID and independently exported submitted input are unavailable. All scoped criteria are checked; ready for local landing. MCP loading remains unverified.

2026-10-03 — Landed on local main with no-ff merge `3300936` (implementation `a7ef41a`, approved design record `ff88203`). Status updated to done after landing. [Round-0 close-out](evidence/T-0000/close-out.md) records chain analysis, evidence summary and retrospective. No remote is configured; nothing was pushed.
