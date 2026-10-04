# Round 1 — Verifiability

Reviewer: `/root/review_r1_verifiability`。原始回報如下。

Axis 2：Verifiability。**P0：3、P1：1、P2：0；本軸有 P0 findings。**

此次保持唯讀，未修改檔案、未呼叫其他 agent、未讀取 live spec，也未執行產品或 ChatGPT 試用。

## 輸入與覆蓋範圍

審查基準為 capture 中的 `main`，base 與 HEAD 均為 `c88c649032dd3b737709cc453a3ddc8cf28a6d3e`；已讀取 captured diff、pending changes 與 untracked inventory。

| 輸入 | 實際 SHA-256 |
| --- | --- |
| round-1/spec.en.md | `ba56761d403b655712b5d7e76728475494a70b45aadaa98fa0631fc9a95b9f08` |
| round-1/traceability.md | `04c8e85d3312e73476ef2350c0199ecf42336ce6beb4e68e27fbe95d797d0be0` |
| prompt.md | `d81fcd8f15f87c58b69e0012eab474b6558e065e4d78a087866dfb094fa35bd5` |
| capture.json | `8dc88b54ff5106734abbbaaacbfb3f97c5f332f6a15b3f57f2a7cac73ffac0ed` |
| captured-git.diff | `b82e8e7806a682d249557852514253c793bd193ea54ce7b0bd512fae6a77885a` |

兩份 round-1 輸入與 capture 中全部 16 份 context 檔案的 SHA-256 均吻合。已讀取 frozen prompt、完整 spec 與 matrix，以及 captured Charter、CONTEXT、runtime、harness-reviewer role、workflow、review、language、ADRs；另查閱與判定界線相關的設計研究。

涵蓋 AC-01–AC-20、TR-01–TR-30。以下判定限於可驗證性，不 adjudicate completeness、contract conflict 或 red-team 軸。

## V-01 — P0：選擇與提問的分支條件沒有可重現的判定界線

- **位置：** `inputs/round-1/spec.en.md:95,156,157`；`inputs/round-1/traceability.md:25,26`。
- **Requirement：** AC-07、AC-08；TR-13、TR-14，Route × Contextual/Insufficient selection × S2。
- **證據／反例：** 請求「我要向高中學生介紹 AI，請推薦簡報風格」提供用途與受眾，但沒有表達需求。回答 A 選擇忘形流並以容易理解為由；回答 B 詢問要偏重概念理解、產品展示還是資料比較。A 可主張資訊已足夠，B 可主張沒有「meaningful selection basis」。spec 與 matrix 都未提供能裁定兩者的分支判準。
- **影響：** 同一 captured request 的「直接選擇」與「先澄清」可能各自被判 pass；無法可靠判定 redundant interview 或必要 clarification。
- **限縮修正：** 定義「足夠資訊」的可觀察條件，例如所提供資訊能否連到至少一個已宣告的表達 focus，並列出資訊不足與邊界案例及預期分支。允許多個合理的 style 結果，但固定何時應交付、何時應提問；理由須指出實際提供的資訊與所選 focus 的關聯。不需指定唯一最佳風格或固定理由字數。
- **不確定性：** 高信心。ticket 可以補案例，但目前補出的判準將決定 AC-07/08 的意義，而不只是測試實作方式。

## V-02 — P0：核心識別與調整相容性的語意判準尚未可觀察化

- **位置：** `inputs/round-1/spec.en.md:77,102,152,159,160`；`inputs/round-1/traceability.md:29,30`。
- **Requirement：** AC-03、AC-10、AC-11；TR-03–TR-07、TR-17、TR-18，All styles × Core identity/Adjustment × S1/S2。
- **證據／反例：** 請求「高橋流保留大字主視覺，另允許圖表與三行輔助註解」。一份 guidance 接受此非核心調整，要求圖表與註解維持次要；另一份回覆認為它增加 competing detail、破壞 compact phrasing，提出減少註解的建議。表中的 `little competing detail` 與 AC 的 `preserving core identity` 未提供接受／衝突的共同界線。僅列入 `core_rules` 也不能證明其內容已保留表中要求的辨識特徵。
- **影響：** 是否需要 conflict explanation、設定是否偷偷覆寫核心，以及風格差異是否成立，會依 reviewer 對形容詞的理解改變。
- **限縮修正：** 要求每個 identifying core rule 宣告可觀察的不變條件、適用條件，以及相容與衝突的例子；驗收檢查回覆有無保留該條件、指出被衝突的 `rule_id`、提出仍滿足它的建議。為 AC-03 加入各風格必須呈現的表達關係與不合格反例。可用「主要／次要焦點」「圖像是否承載指定觀點關係」等關係判準，不必新增固定字數、密度或圖表禁令。
- **不確定性：** 中高信心。style table 已提供方向與重要反禁令；finding 是其不足以裁定邊界調整，不是要求作者風格具備數值公式。

## V-03 — P0：互補輸出與語意等價尚無共同的 semantic oracle

- **位置：** `inputs/round-1/spec.en.md:120,123,154,162,163,186`；`inputs/round-1/traceability.md:35`。
- **Requirement：** AC-05、AC-12、AC-13、AC-14；TR-10、TR-19、TR-22、TR-23，Guidance × Meaning/Conditions × S1/S2。
- **證據／反例：** Markdown 說明某規則只在口述投影時使用短句，並對獨立閱讀保留說明文字；settings 只有「使用精簡文字」。一位 reviewer 可以認為 settings 遺漏了 essential condition，另一位可以認為條件由互補 Markdown 提供即可。schema 僅有自然語言 `constraint`，未標示哪些條件必須跟隨規則保留於 settings。直接／routed、YAML／JSON 的 `same rule meaning` 同樣沒有列出必須維持的命題與容許變動。
- **影響：** 相同 `rule_id`、正確 schema 與可解析格式，不足以產生可重現的語意一致性 verdict；不同 reviewer 可能對「互補」與「遺漏必要條件」得到相反結果。
- **限縮修正：** 在每個規則的來源文件中明列不可省略的規範命題、影響適用範圍的條件，以及可留在 Markdown 的說明／例子。驗收按 `rule_id` 對照這些命題，固定 required rule coverage 與允許的措辭變化。由同一份 oracle 比較直接／routed、YAML／JSON 與不同語言；不要求逐字一致或兩次模型輸出完全相同。
- **不確定性：** 中高信心。spec 已正確排除 exact prose equality；缺口是排除逐字比較後，尚未提供替代的 observable semantic criteria。

## V-04 — P1：實際試用的結果彙整與重試規則未定義

- **位置：** `inputs/round-1/spec.en.md:167,182,195`；`inputs/round-1/traceability.md:40`。
- **Requirement：** AC-18；TR-28，Product validation × Actual ChatGPT evidence × S2。
- **證據／反例：** 相同 skill revision、request 與 host 的第一次試用輸出合法 YAML，第二次輸出 malformed YAML。兩次均被記錄後，AC-18 的「cover」已達成，但未定義該案例、criterion 與當期 release evidence 應如何彙整；亦未定義修正／重試後是否保留先前失敗。
- **影響：** 可以選擇性引用成功回覆，或將「已試用」誤讀成行為已 pass。這不表示必須保證模型每次成功。
- **限縮修正：** 在 ticket 的已核准 test plan 中固定案例、執行／重試政策、每次觀察的 verdict 與 criterion 彙整規則；保留失敗及後續修正的 revision，區分 pass、fail、未驗證。只對記錄的 host/model/revision 宣告結果，不需在此 spec 發明任意次數或成功率。
- **不確定性：** 中等信心。spec 已保留 test-plan approval gate，因此可在 ticket 內完成，列 P1 carryover。

其餘 AC 的計數、禁止行為、來源標示、明確指定、單一風格、格式／欄位、語言及 evidence-status 部分具有可查核的外部觀察；AC-17 的 style distinction 與 handoff consistency 判定則受 V-02、V-03 影響。以上 findings 不以 exact prose、hidden reasoning 或假定內部工具順序作為驗收要求。
