---
id: T-0014
title: "Check collection completeness and deliver acceptance evidence"
epic: 0001-style-guidance
status: done
blocked_by: [T-0013]
---

# T-0014: Check collection completeness and deliver acceptance evidence

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

A user can inspect five skills, distinct identities, source limits, scope, discoverability, references, and handoff consistency. Link every AC to applicable document checks and actual ChatGPT observations for the release candidate. Reuse qualifying evidence only for applicable revisions/behaviors; run approved missing/affected cases. Preserve failures/reruns and report pass/fail/unverified honestly. State Skills MCP loading separately; an unverified loading status is permitted by AC-19 and needs no server/connection development.

## Change objectives

1. Collection-level guidance/source/contract completeness review.
2. Versioned first-release acceptance evidence handoff.

## Acceptance criteria

Traceability contributions: TR-01, TR-02, TR-03, TR-04, TR-05, TR-06, TR-07, TR-08, TR-09, TR-10, TR-11, TR-12, TR-13, TR-14, TR-15, TR-16, TR-17, TR-18, TR-19, TR-20, TR-21, TR-22, TR-23, TR-24, TR-25, TR-26, TR-27, TR-28, TR-29, TR-30, TR-31, TR-32, TR-33, TR-34.
Referenced specification criteria: AC-01, AC-02, AC-03, AC-04, AC-05, AC-06, AC-07, AC-08, AC-09, AC-10, AC-11, AC-12, AC-13, AC-14, AC-15, AC-16, AC-17, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Collection review checks all five skills, distinct identities, source/rule records and limits, scope, descriptions, references, and handoff consistency.
- [x] Every AC-01–AC-20 has revision-applicable document/actual-ChatGPT evidence under an approved case/retry policy; failures/reruns remain, missing checks are unverified, and Skills MCP product loading is stated separately without requiring server/connection work.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Final candidate/coverage audit and approved missing/affected actual trials. Successful retries do not erase failures for the same revision. Evidence remains limited to named content revisions and observed host/model surfaces.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 五個 skills 的整體文件稽核。
2. 首版驗收證據交付。

文件完整性與真實試用結果分別呈現，MCP 未測就標明。

必須先完成：T-0013。相關來源、文件與試用證據都會一起查核；目前狀態為 done，已完成驗收並合併至本機 main。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Collection/source/contract review and all 20 AC mappings complete.
Independent Spec P1 corrected: T13 CT04 remains failed; new Gates candidate with
separate accepted preferences passed one affected actual case. Final local suite
26 pass; independent reviews have no remaining blocker; P2 wording fixed.
See evidence/T-0014 and [security review](../../.proj.specs/0001-style-guidance/review/security-T-0014.md).
Landed on local main. MCP loading unverified.
