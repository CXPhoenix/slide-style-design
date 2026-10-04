---
id: T-0001
title: "Add independently usable Jobs core guidance"
epic: 0001-style-guidance
status: done
blocked_by: [T-0000]
---

# T-0001: Add independently usable Jobs core guidance

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

A direct caller obtains jobs.single_focus through the existing Markdown/YAML contract. Text/visual elements support one stated display, benefit, reveal, or comparison point. Source records distinguish observations from project synthesis, with conditions and compatible/conflicting examples. Several objects can support one comparison; unrelated primary claims conflict with the core. Do not invent a mandatory whole-deck narrative or creator-backed timing formula.

## Change objectives

1. Independently usable, source-attributed Jobs core guidance.

## Acceptance criteria

Traceability contributions: TR-02, TR-04, TR-08, TR-09, TR-19, TR-20, TR-21, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Direct-use Jobs guidance contains jobs.single_focus and all required propositions relating text/visual elements to one stated display, benefit, reveal, or comparison point.
- [x] The rule record traces observations and synthesis, states conditions and boundary examples, avoids unsupported narrative/timing claims, and uses the established Markdown/YAML contract.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Source/document review and actual direct-use ChatGPT core trials verify the identifying relationship and existing handoff. This ticket does not add adjustment response handling.

The concrete test plan table must be approved before tests are written. The [test plan](evidence/T-0001/test-plan.md) is approved; execution evidence and incomplete gates are recorded separately. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 賈伯斯流核心指引。

所有元素支持同一展示／比較焦點，沿用既有交接格式。

必須先完成：T-0000。相關來源、文件與試用證據都會一起查核；T-0000 已完成；本票測試計畫已核准，核心指引、本機測試與文件審查已完成，兩個實際 ChatGPT 回覆已通過稽核，並以 no-ff 合併至本機 main。詳見[覆蓋表](evidence/T-0001/coverage.md)與[試驗步驟](evidence/T-0001/chatgpt-trials.md)。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-03 — User explicitly invoked `$implement T-0001`. Branch `tickets/T-0001/jobs-core` created from clean main (`593b9d2`). Accepted spec/matrix hashes verified; T-0000 is done. [Test plan](evidence/T-0001/test-plan.md) proposed; no tests or product implementation written before approval.

2026-10-03 — User replied A, approving the complete test plan, fixed cases and execution/retry policy. Begin TDD at the established S1/S2 seams.

2026-10-03 — Implemented Jobs core/source and existing Markdown/YAML handoff through three recorded red/green cycles. Full suite: four tests passed; portable verifier and diff check passed. Independent reviews identified one stale ticket-summary issue on each axis; corrected. See [change review](evidence/T-0001/change-review.md), [security review](../../.proj.specs/0001-style-guidance/review/security-T-0001.md), [coverage](evidence/T-0001/coverage.md) and [ChatGPT inputs](evidence/T-0001/chatgpt-trials.md). Actual CT-01/CT-02 remain unverified; no commit or landing yet.

2026-10-04 — User supplied CT-01/CT-02 complete responses. Both passed structural and semantic audit; product/input hashes unchanged. [Results](evidence/T-0001/trial-results.md) retain evidence limits: exact model ID unknown, no independent submitted-input export. All scoped criteria checked; ready to land. MCP remains unverified.

2026-10-04 — User separately confirmed both trials use default conversation model / medium. Manifest and results updated without inferring exact model identity.

2026-10-04 — Landed on local main through no-ff merge `125bf9f` (implementation `2efed76`). Status changed to done after landing. No remote is configured; nothing pushed. This closes T-0001 only; remaining epic tickets and Skills MCP loading are not declared complete.
