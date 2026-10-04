---
id: T-0008
title: "Honor explicit JSON requests with the same rule contract"
epic: 0001-style-guidance
status: done
blocked_by: [T-0001, T-0002, T-0003]
---

# T-0008: Honor explicit JSON requests with the same rule contract

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Explicit JSON requests change serialization, not fields, types, rule IDs, propositions, or conditions. Otherwise YAML remains the default. Completed guidance emits Markdown and exactly one structured format. Handle the existing record shape, including adjustable records when present, without implementing adjustment behavior here.

## Change objectives

1. JSON serialization selection for existing guidance.

## Acceptance criteria

Traceability contributions: TR-09, TR-19, TR-20, TR-21, TR-22, TR-23, TR-28, TR-33.
Referenced specification criteria: AC-05, AC-12, AC-13, AC-14, AC-18, AC-19. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] An explicit JSON request produces parseable JSON with the existing schema, rule IDs, propositions and conditions; otherwise YAML remains the default.
- [x] Completed guidance contains Markdown and exactly one structured representation; equivalent catalog checks, including scope-changing conditions and applicable existing adjustable records, pass across YAML/JSON.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Parsing and actual ChatGPT format-selection trials compare the same catalog checklist across YAML/JSON, including a scope-changing condition. Integration covers subsequently added adjustment/routing combinations.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 指定 JSON 的格式切換。

同一規則改用 JSON，保留欄位、ID 與意思。

必須先完成：T-0001、T-0002、T-0003。相關來源、文件與試用證據都會一起查核；狀態 done，本機與 ChatGPT 驗收完成，Skills MCP 未驗證。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Approved concrete test plan before one red/green cycle; full17 local tests, verifier, whitespace checks pass. Independent Standards/Spec/security reviews complete (table P2 corrected/rechecked). CT-01/02 passed actual ChatGPT semantic and parsing checks; [coverage](evidence/T-0008/coverage.md), [manifest](evidence/T-0008/trial-manifest.json), [security](../../.proj.specs/0001-style-guidance/review/security-T-0008.md). MCP unverified; ready to land.

2026-10-04 — Landed on main: implementation c2b5935, merge 8a78eb1.
