---
id: T-0003
title: "Add independently usable Gates core guidance"
epic: 0001-style-guidance
status: done
blocked_by: [T-0000]
---

# T-0003: Add independently usable Gates core guidance

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

A direct caller obtains gates.evidence_relation through the existing Markdown/YAML contract. Evidence, quantities, or system elements relate to a stated comparison/system point; preserve labels, units, assumptions, and qualifications needed to interpret supplied evidence. Source records state project synthesis, conditions, and compatible/conflicting examples, without an official-method or mandatory-density claim.

## Change objectives

1. Independently usable, source-attributed Gates core guidance.

## Acceptance criteria

Traceability contributions: TR-02, TR-06, TR-08, TR-09, TR-19, TR-20, TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Direct-use Gates guidance contains gates.evidence_relation with stated evidence/comparison/system relationships and all interpretation-critical labels, units, assumptions, and qualifications when applicable.
- [x] Rule records identify project synthesis and evidence limits, with conditions and boundary examples, without an official-method or mandatory-density claim; use the established handoff.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Source/document review and actual direct-use ChatGPT core trials verify analytical relationships, necessary qualifiers, and the established handoff. Adjustment response handling remains separate.

The concrete test plan table must be approved before tests are written. The [test plan](evidence/T-0003/test-plan.md) is approved; actual results are recorded separately. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 比爾蓋茲流核心指引。

證據／數值／系統連到分析重點，保留必要條件。

必須先完成：T-0000。相關來源、文件與試用證據都會一起查核；T-0000 已完成，本票已建立分支，測試計畫已核准，核心與本機驗證已完成，新版兩案實際 ChatGPT 試驗均通過，已合併至本機 main，狀態為 done。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — User explicitly invoked `$implement T-0003`. Branch `tickets/T-0003/gates-core` created from clean main (`ec426c8`). Frozen spec/matrix hashes verified; T-0000 done. [Test plan](evidence/T-0003/test-plan.md) proposed, no tests/product implementation before approval.

2026-10-04 — User replied A, approving the complete test plan and execution/retry policy. Begin TDD at existing S1/S2.

2026-10-04 — Core/source and existing handoff implemented via three red/green cycles. [Coverage](evidence/T-0003/coverage.md) and [trial inputs](evidence/T-0003/chatgpt-trials.md) distinguish local checks from pending actual ChatGPT. Independent reviews precede commit.

2026-10-04 — Independent [change review](evidence/T-0003/change-review.md) has zero actionable findings and one non-blocking duplication smell. [Security review](../../.proj.specs/0001-style-guidance/review/security-T-0003.md) has zero qualifying candidates. Full suite eight tests passed. Actual ChatGPT pending; processing, no commit or landing.

2026-10-04 — Actual candidate 01: CT-01 failed AC-02 (appendix relocation/detail splitting); CT-02 passed. Both default model/medium, exact model unknown. Full evidence retained. Entry boundary clarified; candidate 02 reruns both unchanged requests before closure.

2026-10-04 — Candidate 02 actual CT-01 and CT-02 passed all approved checks; user confirmed both default model/medium, exact model unknown. [Results](evidence/T-0003/results.md), full replies/hashes and [coverage](evidence/T-0003/coverage.md) recorded; candidate 01 failure retained. Product unchanged since targeted reviews. Skills MCP remains unverified. Ready to land; status changes after merge.

2026-10-04 — Landed on local main via merge `26267d9b32f9f70f8cff087cd6d4b8f38a0f24fa` (implementation `8a1b0a8`). Status updated to done after landing. One change objective completed; Skills MCP still unverified.
