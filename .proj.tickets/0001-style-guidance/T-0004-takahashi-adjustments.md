---
id: T-0004
title: "Handle Takahashi adjustments and core conflicts"
epic: 0001-style-guidance
status: done
blocked_by: [T-0000]
---

# T-0004: Handle Takahashi adjustments and core conflicts

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Accepted non-core changes retain text priority and every applicable core condition in both representations. Explicitly subordinate charts/notes remain compatible. A core-replacing request receives the rule ID, conflicting request, broken proposition, and a retaining suggestion. Keep original core settings; do not apply conflicting overrides or unaccepted alternatives. Attribute every declared adjustable rule.

## Change objectives

1. Apply compatible non-core Takahashi adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

## Acceptance criteria

Traceability contributions: TR-02, TR-03, TR-08, TR-09, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Compatible non-core Takahashi changes appear in both representations while retaining all core propositions/conditions; explicitly subordinate chart/note requests are compatible.
- [x] A core-replacing request names the rule ID, conflicting request and broken proposition, offers a retaining suggestion, keeps the original core, and excludes conflicting overrides and unaccepted alternatives.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings, including applicable conditions.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 高橋流相容調整。
2. 高橋流核心衝突回應。

輔助圖表可接受；圖表取代詞句主角時說明衝突。

必須先完成：T-0000。相關來源、文件與試用證據都會一起查核；已建立 ticket 分支，測試計畫已核准，相容／衝突指引與本機檢查已完成；實際 ChatGPT 兩案通過，已合併至本機 main，狀態為 done。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — User invoked `$implement T-0004`. Branch `tickets/T-0004/takahashi-adjustments` from clean main `6e8e64c`. T-0000 done; accepted spec/matrix hashes unchanged. [Test plan](evidence/T-0004/test-plan.md) proposed; no tests or product changes before approval.

2026-10-04 — User replied A, approving all test-plan rows, fixed cases and retry policy. Begin TDD at existing S1/S2.

2026-10-04 — Two scoped red/green cycles completed. [Coverage](evidence/T-0004/coverage.md): full suite 10 passed, actual CT-01/02 pending. [Inputs and evidence](evidence/T-0004/chatgpt-trials.md) prepared. Independent review before commit; processing, not done.

2026-10-04 — Independent [change review](evidence/T-0004/change-review.md): zero actionable findings, one non-blocking duplication smell. [Security review](../../.proj.specs/0001-style-guidance/review/security-T-0004.md): zero qualifying candidates. Snapshot unchanged. Actual ChatGPT pending; no commit/landing/closure yet.

2026-10-04 — Actual CT-01 and CT-02 passed all approved checks; user separately confirmed default model/medium, exact model unknown. [Results](evidence/T-0004/results.md) retain complete replies/hash/verdict. Product unchanged since independent review. Ready to land; status update follows merge. MCP still unverified.

2026-10-04 — Landed on local main via merge `5eb2f99ed41700997b6e72a287f3f1c0a1b3fd17` (implementation `82a9089`). Status changed to done after landing. Both approved objectives complete; Skills MCP unverified.
