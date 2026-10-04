# 公開資料揭露查核

日期：2026-10-04。原始查核基準：本機 `main`，HEAD `81f54a0`。本次交付以匿名化公開快照重建 `main`，舊 Git 目錄與全部 refs 的 bundle 私下保存。這是公開資料與隱私查核，不是完整相依性安全稽核。

## 結論與發布限制

**原始版本有私人資訊揭露；已處理公開快照的已識別問題，並依使用者核准建立乾淨的公開 Git 歷史。** 原始 Git 目錄與經驗證的 all-ref bundle 保留於 gitignored 私人備份，不納入公開歷史。已知模式掃描通過仍不能保證不存在未知格式的資訊揭露。

查核包含 1,188 個原追蹤檔案、49 個可達 commits、1,427 個 Git objects／947 個 unique blobs。第一位 reviewer 逐張檢視 33 張 PNG；第二位 reviewer 獨立核對文字、HTML 與 commit metadata，但未重新目視全部圖片。另以 GitHub API 確認 `CXPhoenix/slide-style-design` 為 public，並以 `git ls-remote` 確認當下沒有公開 branch／tag refs；已依使用者提供的網址設定 `origin`，再次確認沒有公開 branch／tag refs；未推送。未查核外部 fork 或快取。

## 已確認問題

| 編號 | 等級 | 發現與證據位置 | 處理狀態 |
|---|---|---|---|
| D-01 | Medium | `.proj.tickets/0001-style-guidance/evidence/` 中 33 張完整畫面與 15 個 AX 檔案。T-0011–T-0014 的 18 張 PNG 含無關側欄；早期 15 張仍有帳戶／宿主 UI。例：T-0014 的原始 `chatgpt-CT-01-ax.txt` 第 27、44、83 行。 | PNG 改為私人保存；AX 改為僅含助理回覆的公開衍生片段。 |
| D-02 | Medium | `.proj.specs/0001-style-guidance/reports/first-release-acceptance.html` 原第 3 行內嵌 PNG，雜湊與 T-0014 原始畫面一致。 | 移除整個內嵌畫面，不只修改文字。 |
| D-03 | Low | 26 檔、53 次帶 scheme 的私人對話 URL；計入 AX 中無 scheme 的位址共 320 次出現，含重複。 | 清除完整瀏覽器 UI 與所有已識別格式的私人對話位址。未證實位址可繞過存取權限。 |
| D-04 | Low | 54 個實際專案紀錄、98 次個人 home 路徑。另 8 檔 8 次屬開發 skill 的公開範例／regex，已排除誤報。 | 實際本機路徑改為匿名化標記；不改動無關範例的行為。 |
| D-05 | 已確認、公開授權 | 49 個 commits 的 author／committer 使用機構信箱。 | 使用者另行明確授權相同信箱作公開事件回報管道，因此不將它視為須移除的私人資訊。未改寫作者資料。 |

這些問題是公開工作脈絡與隱私揭露；目前沒有認證繞過或 HIGH 等級漏洞的證據。原始 blob 掃描的常見 API token、GitHub／AWS key、private key、Bearer 與附近高熵候選沒有命中；這不排除未知格式憑證。

## 公開證據與雜湊

原始檔案保存在 `.proj.private-evidence/`，已加入 `.gitignore`，不得作為公開發行內容。此路徑只保存本機私人原件；不是可下載的公開附件。

- 原有獨立 response／rendered 文字未識別到私人側欄資料，可保留。
- 原以完整 AX 作為 response 的案例，公開 `response_sha256` 指向助理回覆片段；`original_response_sha256` 指向私人完整畫面文字。片段保留 AX 文字與程式區塊，不冒稱為原始 Markdown。
- 公開片段保留所有助理回覆回合；未公開使用者輸入區與帳戶 UI。原試驗輸入另有 versioned input files。
- screenshot 欄位改成 `private_capture_basename`，只記錄私人原件識別，不承諾公開檔案存在。
- 歷史 review 的 capture／snapshot 雜湊仍描述原始稽核版本。匿名化後的 metadata 不能用來驗證舊 snapshot 的位元組一致性。
- [修改清單與兩種雜湊](publication-artifacts.json)記錄本次匿名化界線；case 成功、失敗、修正與版本適用判讀未改寫。

## 驗證與後續

本機產品結構／證據契約 26 項測試通過；開發結構檢查通過。第二位 reviewer 亦逐一核對 15 份衍生 AX：助理區段未缺失，包含 T-0012 CT-05 的兩個回合與 T-0011 CT-04 的無標準 footer 情況。14 個案例的公開與原始 response 雜湊均相符。`python3 scripts/verify-public-content.py` 檢查工作目錄中的追蹤檔案與未忽略的新檔案，辨識已知私人對話位址、側欄、個人路徑、原始證據圖片與常見憑證模式。它不掃描 Git 歷史，也不是完整 secret scanner。開發 skill 的公開 fixture 例外已獨立查核。

兩份 README 依 Skills MCP `quill-n-grill` 的 revision、technical genre 與 context-handling 指引修訂。讀者入口按用途、選擇、載入前提、範例與輸出、驗證限制、貢獻分工展開；不把開發稽核流程當成產品使用流程。此 MCP skill 的成功載入不構成本專案產品 skills 的 MCP 載入驗證。

使用者核准保留私人完整歷史，並以已查核的公開快照重建本機 `main` 的 init commit。已先驗證 all-ref bundle，再移出原始 Git 目錄並初始化新目錄；沒有沿用舊物件、branch 或 tag。沒有推送或發布 release。公開文件中的舊 commit 識別字只描述歷史稽核基準；相關原始物件須在私人備份查核，不能承諾在公開歷史解析。

未涵蓋 dangling／unreachable objects、其他遠端 refs、外部副本、未知憑證格式與全部第三方相依性弱點。原件與公開衍生片段也不證明所有 GPT 模型、Skills MCP 載入或投影片產出行為。
