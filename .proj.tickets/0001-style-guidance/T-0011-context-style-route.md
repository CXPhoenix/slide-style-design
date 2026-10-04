---
id: T-0011
title: "Select from focus anchors or ask for missing purpose"
epic: 0001-style-guidance
status: done
blocked_by: [T-0010]
---

# T-0011: Select from focus anchors or ask for missing purpose

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Without a style preference, sufficient context produces one eligible style and a reason citing the supplied anchor and selected focus, without optional-field questions. Multiple eligible anchors need no unique winner. Generic/audience-only requests ask for missing purpose/expression need without invented facts/settings. Preserve explicit-choice precedence and established handoff/language invariants.

## Change objectives

1. Select one eligible style from supplied purpose/expression anchors.
2. Ask for missing purpose/expression information when no anchor is supplied.

## Acceptance criteria

Traceability contributions: TR-13, TR-14, TR-24, TR-28, TR-31.
Referenced specification criteria: AC-07, AC-08, AC-09, AC-15, AC-18, AC-19. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Without a style preference, a supplied focus anchor yields one eligible style and a reason naming the supplied anchor and chosen focus, with no optional-field questions; multiple eligible anchors need no unique winner.
- [x] A generic or audience-only request asks for missing purpose/expression information in the applicable language without invented facts or a profile; fixed branch examples follow the accepted spec.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT concept-explanation, evidence-comparison, multiple-anchor, generic-request, and audience-only cases, including the fixed branch examples.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 根據情境選樣式。
2. 情境不足時澄清。

介紹 AI 可依概念說明選擇；只說受眾是教師則問用途。

必須先完成：T-0010。相關來源、文件與試用證據都會一起查核；狀態 done；已完成驗收並合併至本機 main。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Two approved local TDD cycles and 22 structure tests passed. Independent
Standards/Spec/Security reviews found no blocking issue; see evidence/T-0011/reviews.md.
Actual ChatGPT CT01 submission could not be confirmed because browser control failed;
CT02–05 not submitted. See evidence/T-0011/browser-interruption.md. Ticket remains
processing, not committed or landed. Existing continuous-run approval remains valid.

2026-10-04 — Browser recovered; five confirmed actual ChatGPT cases passed. Historical
interruption preserved, actual capture and limitations documented in evidence/T-0011.
All acceptance checks met; commit and local landing pending.

2026-10-04 — Landed on local main: implementation e458a0e, merge 203a3b6. Status done after landing.

2026-10-04 — T14 evidence audit added a canonical link to the existing
[security review](../../.proj.specs/0001-style-guidance/review/security-T-0011.md);
no new security-review execution is claimed.
