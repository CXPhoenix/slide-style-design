---
id: T-0010
title: "Honor explicit styles and report inaccessible guidance"
epic: 0001-style-guidance
status: done
blocked_by: [T-0001, T-0002, T-0003]
---

# T-0010: Honor explicit styles and report inaccessible guidance

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

One small route honors a named supported style despite contrary inferred suitability or missing optional context. Read selected guidance/supporting material as needed and preserve direct-use meaning and the existing handoff. Descriptions distinguish selection from named-style use. Inaccessible guidance produces an honest report without local-tool/MCP assumptions. Contextual selection and unresolved-choice clarification remain separate.

## Change objectives

1. Route an explicit supported choice to that actual style.
2. Report inaccessible selected guidance without fabricating loaded rules.

## Acceptance criteria

Traceability contributions: TR-01, TR-02, TR-10, TR-11, TR-12, TR-19, TR-20, TR-21, TR-22, TR-23, TR-25, TR-26, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Explicit supported style requests reach that actual style without substitution or optional-context questioning; routed use preserves the same identity and existing contract/meaning as direct use.
- [x] Inaccessible guidance receives an honest availability report; loading instructions use relevant support on demand and assume neither local tools nor an MCP connection.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual explicit-route trials for four styles, direct/routed semantic comparisons, optional missing-context and inaccessible-guidance cases. Check current variants; final integration covers the independently added combinations.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 指定樣式的 route。
2. 無法取得指引的回報。

指定 Jobs 就載入 Jobs；取不到指引時清楚回報。

必須先完成：T-0001、T-0002、T-0003。相關來源、文件與試用證據都會一起查核；狀態 done，審查及實際驗收完成，Skills MCP 未驗證。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Approved concrete plan before two document red/green cycles; full20 local tests/verifier/whitespace pass. Independent Standards/Spec/security zero findings. Actual CT01–05 pass, capture/interruption failures retained without model reruns. [Coverage](evidence/T-0010/coverage.md), [manifest](evidence/T-0010/trial-manifest.json), [security](../../.proj.specs/0001-style-guidance/review/security-T-0010.md). MCP unverified; ready to land.

2026-10-04 — Landed on main; implementation08a5064.
