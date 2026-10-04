# 第一輪至第二輪修正紀錄

對照：[完整修正 diff](revision-1-to-2.diff)、[第二輪 input hashes 與自查](round-2-inputs.json)。第一輪快照與四位 reviewer 的原始回報均保留。

| Finding | 限縮修正 | 第二輪對應 |
| --- | --- | --- |
| C-R1-01 | 所有使用者可見回應適用語言規則；矩陣明列 clarification、conflict 與 availability reports。 | AC-15；TR-14–16、TR-24、TR-26 |
| C-R1-02 | mandatory core IDs 固定；其他規則由來源記錄查找，同一 catalog rule 跨語言／格式保持識別碼。 | AC-14；TR-23 |
| V-01 | 明列輸入的 purpose/expression focus anchors；只缺 audience 等選填內容不再提問。列出 AI 介紹、量測比較、泛稱選樣式與 audience-only 的預期分支。 | AC-07/08；TR-13/14、TR-31 |
| V-02 | 明列每種風格 mandatory core record 的必備關係及相容／衝突案例；圖表／註解的數量本身不構成衝突。 | AC-03/10/11/14；TR-17/18、TR-32 |
| V-03 | 規則記錄宣告必備命題與適用條件，作為兩種格式與 direct/routed 的共同核對依據；影響指令適用範圍的條件須留在 constraint。 | AC-05/12/13/14；TR-19/20/23、TR-33 |
| V-04 | 已核准試用計畫預先固定案例及重試規則；失敗與修正版分別保留，逐案例、逐 criterion 彙整 pass/fail/unverified。 | Testing Decisions；TR-28 |
| RT-01 | 呼叫方的 style/format/language/adjustment 指示優先；引用素材中的命令句只作資料，除非呼叫方明確採納。 | Selection and adjustment；TR-34 |

新增的判定方式沒有加入額外樣式、簡報製作責任、MCP transport 或任意數值預設。自查確認：指定風格仍優先，單一主要樣式仍是首版邊界；不以資料完整度迫使已指定的使用者再次選擇；衝突時仍交付原核心規則，建議沒有被當成已採用設定；規範條件同步沒有要求複製全部來源背景；MCP unverified 仍不阻擋已核准的首版驗收。

此紀錄是 parent 的修正與自查說明；是否通過由第二輪四軸回報判定，不以此自查替代獨立審查。
