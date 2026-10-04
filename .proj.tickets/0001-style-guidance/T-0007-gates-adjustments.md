---
id: T-0007
title: "Handle Gates adjustments and core conflicts"
epic: 0001-style-guidance
status: done
blocked_by: [T-0003]
---

# T-0007: Handle Gates adjustments and core conflicts

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Reduced decoration or more whitespace remains compatible while evidence relationships and interpretation-critical qualifiers persist. Removing necessary labels/assumptions receives the required core-conflict explanation and retaining suggestion. Reflect accepted changes consistently, preserve the original core, exclude unaccepted alternatives, and attribute adjustable rules.

## Change objectives

1. Apply compatible non-core Gates adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

## Acceptance criteria

Traceability contributions: TR-02, TR-06, TR-08, TR-09, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Compatible Gates changes retain evidence relationships and interpretation-critical qualifiers consistently in both representations.
- [x] Removing necessary labels/assumptions receives the required conflict explanation and retaining suggestion; original core settings persist without unaccepted alternatives.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings and required qualifiers.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 比爾蓋茲流相容調整。
2. 比爾蓋茲流核心衝突回應。

可增加留白；刪除必要的單位／假設時說明衝突。

必須先完成：T-0003。相關來源、文件與試用證據都會一起查核；狀態 done；沿用已核准測試方式，具體計畫已記錄，指引及本機檢查已完成，實際 ChatGPT 兩例已通過，Skills MCP 未驗證。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Continuous user authorization applies; concrete [test plan](evidence/T-0007/test-plan.md) before tests. T-0003 done, branch tickets/T-0007/gates-adjustments from clean main992ff83.

2026-10-04 — Two scoped red/green cycles; full16 tests pass, verifier/whitespace pass. [Coverage](evidence/T-0007/coverage.md) distinguishes static checks and pending actual CT-01/02. No commit/landing yet.

2026-10-04 — Independent Standards/Spec/security reviews complete; actual CT-01/02 pass, evidence retained. Ready for commit and landing; status stays processing until landed.

2026-10-04 — Landed on main via --no-ff merge; implementation 3a44dca. All ticket gates complete; MCP loading remains unverified.
