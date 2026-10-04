---
id: T-0006
title: "Handle Wangxing adjustments and core conflicts"
epic: 0001-style-guidance
status: done
blocked_by: [T-0002]
---

# T-0006: Handle Wangxing adjustments and core conflicts

## Context

This slice is part of the [approved breakdown](../../.proj.specs/0001-style-guidance/ticket-breakdown.md). Use the [accepted style-guidance specification](../../.proj.specs/0001-style-guidance/spec.en.md) and [traceability matrix](../../.proj.specs/0001-style-guidance/traceability.md) for its scoped requirements. The user approved granularity, blocking edges, and deliverables with “都核准” on 2026-10-03. The audit is limited to the one or two declared change objectives, while inspecting all related implementation, documentation and evidence.

## Deliverable

Color or omitting humor remains compatible while the meaningful text/visual relationship persists. Replacing it with unrelated decoration receives the required conflict explanation and retaining suggestion. Both representations reflect accepted adjustments and conditions, exclude unaccepted alternatives, and retain the original core. Attribute declared adjustable rules.

## Change objectives

1. Apply compatible non-core Wangxing adjustments in guidance/settings.
2. Explain incompatible core changes while retaining the original core.

## Acceptance criteria

Traceability contributions: TR-02, TR-05, TR-08, TR-09, TR-17, TR-18, TR-19, TR-20, TR-23, TR-28, TR-30, TR-32, TR-33.
Referenced specification criteria: AC-02, AC-03, AC-04, AC-05, AC-10, AC-11, AC-12, AC-13, AC-14, AC-18, AC-19, AC-20. These are scoped contributions; a partial increment does not claim that every referenced AC is fully satisfied.

- [x] Compatible Wangxing changes, including color or omitted humor, retain the meaningful viewpoint/visual relationship in both representations.
- [x] Unrelated decoration replacing that relationship receives the required conflict explanation and retaining suggestion; original core settings persist without unaccepted alternatives.
- [x] Document checks and the approved actual-ChatGPT trial observations demonstrate the changed behavior. Keep requests, supplied content revisions, responses, available host/model details, verdicts, failures and reruns; unexecuted checks remain unverified.

## Verification intent

Actual ChatGPT compatible/conflicting boundary trials and semantic checks of adjusted guidance/settings.

The concrete test plan table must be approved before tests are written. This ticket records intended verification, not an approved test plan or a passing result. Preserve established behavior; do not add independent objectives without revising the breakdown.

## 給使用者（zh-TW）

本票的變更目標共 2 項：
1. 忘形流相容調整。
2. 忘形流核心衝突回應。

可不用幽默；無關裝飾取代有意義圖文關係時說明衝突。

必須先完成：T-0002。相關來源、文件與試用證據都會一起查核；狀態為 processing；具體測試計畫沿用已核准方式，指引與本機檢查已完成；實際 ChatGPT 兩案通過，已合併至 main，狀態 done。

## Comments

2026-10-03 — Published after the user approved all three breakdown categories.

2026-10-04 — Continuous implementation and browser trial authorization applies. [Test plan](evidence/T-0006/test-plan.md) documented before tests, T-0002 done. Branch tickets/T-0006/wangxing-adjustments from clean main87f9b48.

2026-10-04 — Independent Standards found stale user-facing implementation status; parent synchronized that line after snapshot check. Spec0 findings; security0 qualifying candidates; product/input unchanged. Actual trials pending.

2026-10-04 — Actual CT-01/02 pass all approved checks, full replies/screenshots/URL/hash recorded. Product unchanged from review. Medium visible, exact model unknown; MCP unverified. Ready to land.

2026-10-04 — Landed on local main merge b904d7059b203cb170cba2a5f91e896c0373476a; done after landing.
