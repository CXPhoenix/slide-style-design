---
id: T-0002
title: "Add independently usable Wangxing core guidance"
epic: 0001-style-guidance
status: done
blocked_by: [T-0000]
---

# T-0002: Add independently usable Wangxing core guidance

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

A direct caller obtains wangxing.text_visual_relation through the existing Markdown/YAML contract. Concise viewpoint text and a meaningful visual relationship communicate the same viewpoint and aid understanding. Source records include classification, conditions, evidence limits, and compatible/conflicting examples. Identify 張忘形, not 王興; humor, monochrome appearance, and oral-only use are not mandatory.

## Change objectives

1. Independently usable, source-attributed 張忘形 core guidance.

## Acceptance criteria

Traceability contributions: TR-02, TR-05, TR-08, TR-09, TR-19, TR-20, TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Direct-use guidance identifies 張忘形 and contains wangxing.text_visual_relation with all required viewpoint-to-visual propositions.
- [x] Source classification, conditions, limits, and boundary examples are recorded; humor, monochrome, and oral-only use are not universal requirements; use the established Markdown/YAML contract.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Source/document review and actual direct-use ChatGPT core trials verify identity and the existing handoff. Adjustment response handling remains separate.

The concrete test plan table must be approved before tests are written. The [test plan](evidence/T-0002/test-plan.md) is approved; actual results are recorded separately. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 忘形流核心指引。

精簡觀點與有意義的視覺關係，沿用既有交接格式。

必須先完成：T-0000。相關來源、文件與試用證據都會一起查核；T-0000 已完成，本票已建立分支，測試計畫已核准，核心與本機驗證已完成，兩份實際 ChatGPT 回覆已通過稽核，並合併至本機 main。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — User explicitly invoked `$implement T-0002`. Branch `tickets/T-0002/wangxing-core` created from clean main (`7eef89b`). Frozen spec/matrix hashes verified and T-0000 done. [Test plan](evidence/T-0002/test-plan.md) proposed; no tests or product implementation before approval.

2026-10-04 — User replied A, approving the complete test plan and execution/retry policy. Begin TDD at S1/S2.

2026-10-04 — Core/source and existing handoff implemented through three red/green cycles. Structure checks passed; [coverage](evidence/T-0002/coverage.md) and [trial inputs](evidence/T-0002/chatgpt-trials.md) distinguish local verification from pending actual ChatGPT. Independent change/security reviews follow before committing.

2026-10-04 — Independent [Standards/Spec review](evidence/T-0002/change-review.md) has zero actionable findings; test duplication retained as one non-blocking smell. [Security review](../../.proj.specs/0001-style-guidance/review/security-T-0002.md) has zero qualifying candidates. Full suite: six tests passed. Actual ChatGPT remains pending; status processing, no commit or landing.

2026-10-04 — User supplied both complete responses and confirmed default conversation model / medium. Structural and semantic checks passed; hashes unchanged. [Results](evidence/T-0002/trial-results.md) retain exact-model and submitted-input evidence limits. All scoped criteria checked; ready to land. MCP loading unverified.

2026-10-04 — Landed on local main with no-ff merge `b1fd32e` (implementation `ace5b33`). Status done after landing. No remote configured, nothing pushed. This closes T-0002 only; full epic and Skills MCP loading are not declared complete.
