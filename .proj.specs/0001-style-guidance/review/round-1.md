# 第一輪 adversarial review

日期：2026-10-03。四位 reviewer 各自審查一軸，使用相同 frozen prompt、同一份 spec/matrix 與背景快照；受 concurrency 限制分批執行。

| 軸 | 原始報告 | P0 | P1 | P2 |
| --- | --- | --- | --- | --- |
| Completeness | [完整性](round-1-completeness.md) | 0 | 2 | 0 |
| Verifiability | [可驗證性](round-1-verifiability.md) | 3 | 1 | 0 |
| Contract conflict | [契約衝突](round-1-contract.md) | 0 | 0 | 0 |
| Red team | [Red team](round-1-redteam.md) | 0 | 1 | 0 |
| 合計 | | 3 | 4 | 0 |

第一輪未通過：3 個 P0 尚待修正。不同軸的回報沒有對同一要求提出互斥的結論，不需以投票裁定。

| Finding | 原等級 | 待修正內容 |
| --- | --- | --- |
| C-R1-01 | P1 | 語言要求追溯至澄清與無法載入的回應。 |
| C-R1-02 | P1 | 同一規則的識別碼跨語言與序列化保持相同。 |
| V-01 | P0 | 明列 route 何時直接選擇、何時提問的可觀察分支與案例。 |
| V-02 | P0 | 核心規則的必備關係、相容與衝突案例，避免靠密度形容詞判定。 |
| V-03 | P0 | 規則的必備命題與條件作為雙格式、direct/routed 與跨語言的核對依據。 |
| V-04 | P1 | 試用計畫預先固定案例與重試方式，保留失敗，明列結果彙整。 |
| RT-01 | P1 | 區分使用者對 skill 的要求與引用素材中的命令句。 |

修正只補足已核准要求的判定邊界，不增加簡報製作、MCP transport 或固定數值門檻。修正版交給第二輪四軸審查；提示不變，只有 spec 版本（含 matrix）改變。本報告不是產品試用結果。
