# Slide Style Design tickets

使用者於 2026-10-03 回覆「都核准」，已核准 15 張票的粒度、依賴與交付配置。每票一至兩個可獨立稽核的變更目標。

[核准的工作分解](../.proj.specs/0001-style-guidance/ticket-breakdown.md) · [中文 spec](../.proj.specs/0001-style-guidance/spec.zh-TW.md) · [Traceability matrix](../.proj.specs/0001-style-guidance/traceability.md)

## 初始工作清單

全部票的 frontmatter 狀態為 `todo`；阻擋狀態由 `blocked_by` 指向的票是否 `done` 推導。初始只有 T-0000 可開始，後續以各票的最新 frontmatter 判定。

| 票號 | 變更目標 | 項數 | Blocked by |
| --- | --- | --- | --- |
| [T-0000](0000-walking-skeleton/T-0000-walking-skeleton.md) | 高橋流核心指引；Markdown＋YAML 交接契約 | 2 | 無 |
| [T-0001](0001-style-guidance/T-0001-jobs-core.md) | 賈伯斯流核心指引 | 1 | T-0000 |
| [T-0002](0001-style-guidance/T-0002-wangxing-core.md) | 忘形流核心指引 | 1 | T-0000 |
| [T-0003](0001-style-guidance/T-0003-gates-core.md) | 比爾蓋茲流核心指引 | 1 | T-0000 |
| [T-0004](0001-style-guidance/T-0004-takahashi-adjustments.md) | 高橋流相容調整；高橋流核心衝突回應 | 2 | T-0000 |
| [T-0005](0001-style-guidance/T-0005-jobs-adjustments.md) | 賈伯斯流相容調整；賈伯斯流核心衝突回應 | 2 | T-0001 |
| [T-0006](0001-style-guidance/T-0006-wangxing-adjustments.md) | 忘形流相容調整；忘形流核心衝突回應 | 2 | T-0002 |
| [T-0007](0001-style-guidance/T-0007-gates-adjustments.md) | 比爾蓋茲流相容調整；比爾蓋茲流核心衝突回應 | 2 | T-0003 |
| [T-0008](0001-style-guidance/T-0008-json-settings.md) | 指定 JSON 的格式切換 | 1 | T-0001、T-0002、T-0003 |
| [T-0009](0001-style-guidance/T-0009-language-consistency.md) | 說明語言與 ID 一致性 | 1 | T-0001、T-0002、T-0003 |
| [T-0010](0001-style-guidance/T-0010-explicit-style-route.md) | 指定樣式的 route；無法取得指引的回報 | 2 | T-0001、T-0002、T-0003 |
| [T-0011](0001-style-guidance/T-0011-context-style-route.md) | 根據情境選樣式；情境不足時澄清 | 2 | T-0010 |
| [T-0012](0001-style-guidance/T-0012-style-choice-clarification.md) | 名稱不明／不支援的澄清；多種主要樣式的澄清 | 2 | T-0010 |
| [T-0013](0001-style-guidance/T-0013-quoted-material-boundary.md) | 使用者指令與引用素材的界線 | 1 | T-0004、T-0005、T-0006、T-0007、T-0008、T-0009、T-0011、T-0012 |
| [T-0014](0001-style-guidance/T-0014-release-evidence.md) | 五個 skills 的整體文件稽核；首版驗收證據交付 | 2 | T-0013 |

T-0000 先建立高橋流核心指引與 Markdown＋YAML 的最小 ChatGPT 使用路徑。各票具體 test plan table 尚待實作階段提出與核准；工作分解核准不代表測試已執行或產品已驗收。
