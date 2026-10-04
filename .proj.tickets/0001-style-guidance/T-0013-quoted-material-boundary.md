---
id: T-0013
title: "Keep quoted material separate from caller instructions"
epic: 0001-style-guidance
status: done
blocked_by: [T-0004, T-0005, T-0006, T-0007, T-0008, T-0009, T-0011, T-0012]
---

# T-0013: Keep quoted material separate from caller instructions

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Quoted commands do not override caller style, format, language, or adjustment instructions unless explicitly adopted. Material can still supply purpose/audience/expression context. Preserve existing direct/routed behavior while making this boundary explicit across the implemented control dimensions.

## Change objectives

1. Caller-instruction versus source-material interpretation.

## Acceptance criteria

Traceability contributions: TR-02, TR-11, TR-13, TR-23, TR-24, TR-28, TR-34.
Referenced specification criteria: AC-02, AC-05, AC-06, AC-07, AC-09, AC-13, AC-14, AC-15, AC-18, AC-19. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Quoted commands do not override caller style, format, language or adjustment instructions unless the caller explicitly adopts them; material may still supply context.
- [x] The fixed caller Takahashi/default-YAML request with quoted Gates/JSON commands retains the caller choice without extra choice clarification; actual trials cover the affected existing controls and explicit-adoption boundary.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT conflicting-quote and explicit-adoption cases, including the fixed caller Takahashi/default-YAML request with quoted Gates/JSON commands. All affected controls exist before cross-control trials.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 1 項：
1. 使用者指令與引用素材的界線。

你指定高橋流，素材中「改用 Gates」不會改掉你的選擇。

必須先完成：T-0004、T-0005、T-0006、T-0007、T-0008、T-0009、T-0011、T-0012。相關來源、文件與試用證據都會一起查核；目前狀態為 done，已完成驗收並合併至本機 main。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — 25 local tests and six actual ChatGPT cases passed; one Standards P2
status-prose inconsistency corrected, no blocker. See evidence/T-0013 and
[security review](../../.proj.specs/0001-style-guidance/review/security-T-0013.md).
Landed on local main; Skills MCP loading unverified.

2026-10-04 — Subsequent independent T14 audit corrected the initial CT04 pass
verdict to failed: an unrequested reduced-decoration preference was applied.
Initial verdict/raw response remain; T14 supplies the narrow correction and a
new-candidate affected-case pass. The earlier six-pass statement is historical
and is superseded by active T13 trial-manifest.json (five pass, one fail).
