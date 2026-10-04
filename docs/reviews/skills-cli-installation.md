# Skills CLI 安裝驗證

日期：2026-10-04。來源：public GitHub repository `CXPhoenix/slide-style-design`。受測 `main` 與 `v0.1.0` 均指向 `374f7b70d191e6ef88ccc701dcb195f259363b4a`；之後的 README 修改不改變產品檔案。

## 方法與環境

使用官方 [vercel-labs/skills](https://github.com/vercel-labs/skills) 的 npm `skills@1.7.0`，Node.js v24.13.0、npm 11.6.2。npm 套件 metadata 的 repository 指向該官方 repo，engine 要求為 Node.js `>=22.20.0`。

每個安裝案例在獨立暫存專案執行；不指定 `--global`，明確指定目標 agent，停用遙測。CLI 從實際 GitHub URL 取得內容，未用本機來源取代遠端。測試執行使用 `npx --yes skills@1.7.0`，README 使用官方慣用的 `npx skills`；驗證結論限於記錄的 CLI 版本。

## 結果

| 編號 | CLI 操作 | 結果 |
|---|---|---|
| INSTALL-01 | `add CXPhoenix/slide-style-design --list` | exit 0；列出 13 個可辨識 skills，包含 5 個產品與開發協作入口。只是列出，未安裝。 |
| INSTALL-02 | `add https://github.com/CXPhoenix/slide-style-design/tree/main/skills --list` | exit 0；只列出 5 個產品。 |
| INSTALL-03 | 上述 `main/skills` URL，加 `--agent codex --skill '*' --yes` | exit 0；專案 `.agents/skills/` 有且只有 5 個產品，共 43 個檔案。 |
| INSTALL-04 | 上述 `main/skills` URL，加 `--agent claude-code --skill '*' --yes` | exit 0；專案 `.claude/skills/` 有且只有 5 個產品，共 43 個檔案。 |
| INSTALL-05 | `add https://github.com/CXPhoenix/slide-style-design/tree/v0.1.0/skills --agent codex --skill jobs-style --copy --yes` | exit 0；專案 `.agents/skills/` 只含 `jobs-style`，共 9 個檔案。 |

INSTALL-03、04 的 43 個檔案與產品來源逐一比對，位元組全部一致；各自 52 個 Markdown 相對連結皆可解析。Route 的 registry 可找到四個樣式入口。INSTALL-05 的 9 個檔案亦一致，10 個相對連結可解析。

所有已安裝檔案的名稱集合均與所選產品來源一致，沒有混入開發協作 skills。CLI 的安裝摘要及實際目錄內容均已核對；[結構化結果與產品雜湊](skills-cli-installation.json)保留可公開的驗證資料，不含私人暫存路徑或完整宿主紀錄。

## 範圍與限制

這項驗證證明 CLI 能從遠端辨識並安裝產品檔案，references 與 route 相對路徑在安裝後仍完整。不代表 Codex／Claude Code 的新工作階段已自動發現或執行這些 skills，也不證明模型輸出行為。

沒有測試全域安裝、其他 agents、互動式選擇或未來 CLI 版本。本機 CLI 安裝不是 ChatGPT 網頁版註冊或 Skills MCP 動態載入；產品的 Skills MCP 相容性仍未驗證。既有 v0.1.0 tag、release 與產品定義沒有變動。
