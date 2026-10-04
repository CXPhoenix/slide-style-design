---
id: T-0005
title: "Handle Jobs adjustments and core conflicts"
epic: 0001-style-guidance
status: done
blocked_by: [T-0001]
---

# T-0005: Handle Jobs adjustments and core conflicts

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Color changes or several objects serving one comparison remain compatible. Unrelated competing primary claims receive the required rule ID, conflicting request, broken proposition, and retaining suggestion. Markdown/settings reflect accepted changes, retain all core propositions/conditions, and exclude unaccepted alternatives. Attribute declared adjustable rules.

## Change objectives

1. Apply compatible non-core Jobs adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

## Acceptance criteria

Traceability contributions: TR-02, TR-04, TR-08, TR-09, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Compatible Jobs changes, including objects serving one comparison or changed colors, appear consistently while retaining all core propositions/conditions.
- [x] Competing unrelated primary claims receive the required conflict explanation and retaining suggestion; original core settings persist without unaccepted alternatives.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 賈伯斯流相容調整。
2. 賈伯斯流核心衝突回應。

多個物件可支持共同焦點；無關主張互相競爭時說明衝突。

必須先完成：T-0001。相關來源、文件與試用證據都會一起查核；狀態為 processing；指引已實作，測試 oracle 與紀錄已更正，實際 ChatGPT 兩案通過，已合併至本機 main，狀態為 done。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Continuous execution authorized; [concrete test plan](evidence/T-0005/test-plan.md) instantiates user approval before tests. Branch tickets/T-0005/jobs-adjustments; T-0001 done.

2026-10-04 — Two scoped red/green cycles completed. [Coverage](evidence/T-0005/coverage.md): initial full suite failed due to incorrect fixture core ID; preserved and corrected after review. Actual CT-01/02 pending. [Inputs and evidence](evidence/T-0005/chatgpt-trials.md) prepared. Independent review before commit; processing, not done.

2026-10-04 — Review identified wrong fixture ID and inaccurate pass claims, plus stale style/status oracle wording. Original fixture/logs/claims retained in evidence/T-0005/pre-review-correction. Corrected to approved jobs.single_focus; actual input wording changed before submission. Independent re-review required.

2026-10-04 — Independent review findings resolved; corrected local suite12 passed. Actual Chrome ChatGPT candidate02 CT-01/02 passed at visible Medium; full replies/screenshots/URLs/hash/verdict saved. Product unchanged after review; exact model unknown, MCP unverified. Ready to land.

2026-10-04 — Landed via local main merge `d21816fa0add33d7be19e49d9bf964fb80aca71e`, implementation 4f54ed1. Status done after landing.
