# 貢獻指南

[English](CONTRIBUTING.en.md) · [專案介紹](README.md)

歡迎改善來源、風格判準、範例、翻譯與驗證。本專案提供風格約束；內容改寫、簡報製作、匯出工具與自動混搭不在目前範圍。參與時請遵守[行為準則](CODE_OF_CONDUCT.md)。

## 提出問題或建議

先搜尋既有 issues 與 PR。問題請附上使用的 skill、版本或 commit、宿主可見的模型／推理強度、最小可重現輸入、預期與實際結果。無法辨識模型時請明寫未知。新功能請先說明使用情境、與現有判準的差異及是否超出產品範圍。

**請勿公開私人資料。** 移除真實姓名、聯絡資料、存取憑證、私人連結、瀏覽器側欄與本機路徑。使用虛構素材；只分享與問題相關的回覆區。安全疑慮不要在公開 issue 附上可利用的細節，請使用 repository 的私人漏洞回報功能（若已啟用），或維護者已公開的私人聯絡方式。

## 修改與 PR

1. 從自己的 fork 建立範圍明確的分支；有既有 ticket 時沿用 ticket 分支慣例。
2. 修改 `skills/` 的產品文件；開發協作 skills 位於 `.agents/skills/` 與 `.claude/skills/`，用途不同。
3. 來源優先採創作者或官方公開資料。註明來源支持、案例觀察與專案綜整的差異；不要把推論寫成創作者原話。引用須符合原授權，不要貼入整篇第三方內容。
4. 變更規則時保留穩定識別字，讓 Markdown 與 YAML／JSON 語意一致；補上相容調整、核心衝突及必要限定案例。
5. 執行下列檢查，提供結果與未驗證範圍。README、貢獻指南與行為準則的中英文版本需同步；中文使用台灣繁體中文。
6. PR 說明問題、變更後行為、相關 issue／ticket、來源、驗證與限制。每個 PR 集中處理一個問題，避免夾帶不相關整理。

```sh
python3 -m pip install -r requirements-test.txt
python3 -B -m unittest discover -s tests -v
python3 scripts/verify-project.py
python3 scripts/verify-public-content.py
```

需要 Python 3.11+。本機測試不等於 ChatGPT 行為測試；提供定義後的對話試驗也不等於 Skills MCP 載入驗證。請保留失敗與修正紀錄，不將舊版本試驗宣稱為新版重新執行。公開證據若經匿名化，請記錄公開副本的用途與雜湊界線，勿把它冒稱為原始瀏覽器畫面。

## 使用開發 agent

請讀 `AGENTS.md` 與連結的開發流程。產品規則的實作需沿用已核准的 spec、ticket、測試與 review gates。開發 agent 執行 commit 時，必須使用本專案 `tw-emoji-commit` skill。一般外部貢獻者不需要為小型文件修正安裝整套 agent 工具；維護者會協助確認適用流程。

可以使用 AI 協助，但提交者仍須查核來源、授權、正確性與私人資訊。PR 中請說明足以影響審查的 AI 使用情況，尤其生成的來源判讀或測試證據；不要求揭露私人對話。

## 授權與審查

提交者應有權提供修改；原創貢獻依本專案 MIT License 提供。第三方素材保留原授權，必要時更新 `THIRD_PARTY_NOTICES.md`。目前不要求額外 CLA。維護者可能要求縮小範圍、補充來源或驗證；是否合併依產品範圍與證據而定。
