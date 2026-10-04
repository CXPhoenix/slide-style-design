# 文件導覽

第一次使用，先讀[協作指南](guide.md)，了解如何啟動工作、使用 skills 與交接。以下文件會隨專案保留，初始化後仍可查閱。

[Windows 自動開啟停用公告與自行驗證](security/windows-opener.md)。

## 依工作找文件

| 你遇到的問題 | 文件 |
| --- | --- |
| 開發助理需要遵守哪些共用規則？ | [AGENTS.md](../AGENTS.md) |
| 簡報風格設計的研究與未決問題？ | [風格設計脈絡](research/2026-10-03-style-design-context.md) |
| 首版的行為與驗收條件？ | [英文 spec](../.proj.specs/0001-style-guidance/spec.en.md)、[中文稽核版](../.proj.specs/0001-style-guidance/spec.zh-TW.md) 與 [traceability matrix](../.proj.specs/0001-style-guidance/traceability.md) |
| 首版 spec 的審查結果與通過版本？ | [第二輪四軸審查](../.proj.specs/0001-style-guidance/review/round-2.md)（P0／P1／P2 皆為 0） |
| 產品與協作 skills 的名詞如何區分？ | [領域詞彙](../CONTEXT.md) |
| 從需求到交付，每一步何時可以往下走？ | [交付流程](agents/workflow.md) |
| Spec 與 tickets 放哪裡？狀態怎麼判定？ | [Issue tracker](agents/issue-tracker.md) |
| 四軸 review 與安全審查如何進行？ | [審查規則](agents/review.md) |
| Claude Code 與 Codex 如何共用 skills、交接？ | [Runtime adapters](agents/runtime.md) |
| Claude 各角色用哪個模型？何時委派？ | [Claude 模型分工](agents/claude-orchestration.md) |
| Codex 如何區分 prompt、skill 與宿主能力？ | [Codex 執行指引](agents/codex.md) |
| 哪些文件用英文？中英文規格如何同步？ | [語言規則](agents/language.md) |
| 探索程式碼前，如何閱讀領域模型？ | [領域文件指引](agents/domain.md) |

`agents/` 內的英文文件供開發助理執行流程，也可用來查核工作是否符合規範。面向使用者的說明採台灣繁體中文。

## 設計決策

ADR 保存已採用的決策與理由，方便後續修改時判斷影響。

- [ADR-0001](adr/0001-walking-skeleton-then-epic-loop.md)：先建立 walking skeleton，再以 epic 交付。
- [ADR-0002](adr/0002-ticket-status-in-frontmatter.md)：ticket 狀態存於 frontmatter。
- [ADR-0003](adr/0003-adversarial-review-fixed-axes-two-rounds.md)：規格審查使用固定四軸，最多兩輪。

[Archify 依賴處理與可執行測試](security/archify-dependencies.md)。

T-0000: [高橋流核心入口](../skills/takahashi-style/SKILL.md)、[測試計畫](../.proj.tickets/0000-walking-skeleton/evidence/T-0000/test-plan.md)、[ChatGPT 試驗](../.proj.tickets/0000-walking-skeleton/evidence/T-0000/chatgpt-trials.md)。

T-0001: [賈伯斯流核心入口](../skills/jobs-style/SKILL.md)、[驗證結果](../.proj.tickets/0001-style-guidance/evidence/T-0001/trial-results.md)。

T-0002: [忘形流核心入口](../skills/wangxing-style/SKILL.md)、[驗證結果](../.proj.tickets/0001-style-guidance/evidence/T-0002/trial-results.md)。
