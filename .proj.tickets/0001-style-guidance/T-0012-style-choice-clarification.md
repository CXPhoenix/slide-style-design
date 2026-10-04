---
id: T-0012
title: "Clarify unresolved names and multiple styles"
epic: 0001-style-guidance
status: done
blocked_by: [T-0010]
---

# T-0012: Clarify unresolved names and multiple styles

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Unknown/ambiguous names ask for the intended supported style. Multiple-style or per-page mixing requests ask for one primary style. Do not invent presets, mixing, or a profile before selection. Existing supported choices retain explicit-route behavior and responses follow the shared language rule.

## Change objectives

1. Clarify ambiguous or unsupported named styles within the supported set.
2. Clarify unresolved requests for multiple primary styles.

## Acceptance criteria

Traceability contributions: TR-15, TR-16, TR-24, TR-28.
Referenced specification criteria: AC-08, AC-09, AC-15, AC-18, AC-19. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Ambiguous/unsupported names receive clarification for an intended supported style without inventing a preset.
- [x] Unresolved multiple-style/per-page-mixing requests ask for one primary style, without mixing or a fabricated profile; established supported choices are preserved.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT ambiguous/unsupported-name and multiple-style clarification cases, with no fabricated profile.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 名稱不明／不支援的澄清。
2. 多種主要樣式的澄清。

找不到名稱或要求混搭時，釐清要用哪一種支援樣式。

必須先完成：T-0010。相關來源、文件與試用證據都會一起查核；目前狀態為 done，已完成驗收並合併至本機 main。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Two TDD cycles, 24 local checks and five actual ChatGPT cases passed.
Independent Standards/Spec/Security reviews found no blocker. See evidence/T-0012
and [security report](../../.proj.specs/0001-style-guidance/review/security-T-0012.md).
Landed on local main; Skills MCP loading unverified.
