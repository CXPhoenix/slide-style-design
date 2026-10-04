---
id: T-0009
title: "Preserve user language and stable identifiers"
epic: 0001-style-guidance
status: done
blocked_by: [T-0001, T-0002, T-0003]
---

# T-0009: Preserve user language and stable identifiers

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Visible explanations and constraint text follow requested/conversation language. Chinese uses Taiwan Traditional Chinese. Field names, style IDs, and catalog rule IDs remain English and stable. Translation preserves propositions/conditions. Apply this to existing response types; later routes inherit the same language invariant rather than adding a divergent rule.

## Change objectives

1. Consistent requested-language behavior for guidance.

## Acceptance criteria

Traceability contributions: TR-09, TR-14, TR-15, TR-16, TR-19, TR-20, TR-23, TR-24, TR-26, TR-28, TR-33.
Referenced specification criteria: AC-05, AC-08, AC-09, AC-12, AC-13, AC-14, AC-15, AC-16, AC-18, AC-19. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] All existing visible explanations and constraint text follow requested/conversation language; Chinese uses Taiwan Traditional Chinese.
- [x] English field/style/rule IDs remain stable and unique, while Chinese/English rule text preserves all required propositions and conditions. The invariant applies to later response types as they are added.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual Chinese/English ChatGPT trials and semantic ID/condition checks for existing response types. Final integration checks additional route-response combinations.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 說明語言與 ID 一致性。

中文用台灣繁體中文，英文可換說法，規則 ID 不變。

必須先完成：T-0001、T-0002、T-0003。相關來源、文件與試用證據都會一起查核；狀態 done，審查與實際驗收完成，Skills MCP 未驗證。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — One language objective; concrete approved plan before red/green. Full18 local tests, verifier and whitespace pass; affected test repeated after English example P2 corrections. Independent Standards/Spec rechecked corrections, security zero candidates. Candidate02 CT01/02 actual ChatGPT pass. [Coverage](evidence/T-0009/coverage.md), [manifest](evidence/T-0009/trial-manifest.json), [security](../../.proj.specs/0001-style-guidance/review/security-T-0009.md). MCP unverified; ready to land.

2026-10-04 — Landed on main; implementation574f3fc.
