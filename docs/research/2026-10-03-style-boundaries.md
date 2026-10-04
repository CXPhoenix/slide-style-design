# 簡報風格、資訊密度與 route 的證據界線

查核日期：2026-10-03（Asia/Taipei）。這是需求訪談用的有界研究，並非產品規格。

既定範圍：產品由數個「樣式 skill」與一個「route skill」組成，放在 `skills/`。本文不提出簡報製作流程，不把研究結果視為使用者已核准的產品行為。

## 研究問題與範圍

查核使用者提供的 ChatGPT 提案中，`Style ≠ Theme`、逐頁 `auto` 混搭、`seconds_per_slide: 35`、`max_concepts_per_slide: 1`、`meme_frequency: 6`、`handout_mode` 與 `density` 的依據；另以公開網頁搜尋輕量查找人物流派相關的開源 `SKILL.md`。

學習研究優先使用作者維護的官方網站、作者原始論文及出版者摘要。這些研究多測量科學或技術內容的理解、保留與遷移；不能直接推論說服力、舞臺效果、品牌形象，也不能直接證明四種人物流派孰優孰劣。本文沒有進行系統性文獻回顧、完整 GitHub 程式碼搜尋或 Skills MCP 全站檢索。

## 可確認的學理與適用條件

### 主張與視覺證據有研究脈絡，但不等於人物風格

Assertion-evidence 的作者官方網站區分「主題標題＋條列」與「句子主張＋視覺證據」。作者的研究摘要指出：兩組觀眾聽到相同講述、看到不同投影片，後者的理解與記憶較好。這是技術內容的比較，不能擴張成「所有簡報只能一頁一個概念」或「所有 bullet 均有害」。[作者官方研究頁](https://www.writing.engr.psu.edu/research.html)、[作者官方方法頁](https://www.assertion-evidence.org/)

2013 年論文是 Garner 與 Alley 的 *How the Design of Presentation Slides Affects Audience Comprehension: A Case for the Assertion–Evidence Approach*，刊於 *International Journal of Engineering Education*, 29(6), 1564–1579。搜尋索引可讀到原始論文摘要，其中比較 110 位工程學生；官方 PDF 在本次工具讀取時失敗，因此本文不據此自行補述完整實驗方法或效應量。[原始論文官方 PDF](https://www.writing.engr.psu.edu/ae_comprehension.pdf)

### 「減少負荷」並不是「字越少越好」

Mayer 與 Moreno（2003）把負荷問題拆成不同情境，例如必要內容太複雜、無關內容占用處理能力，以及畫面與口述的重複或分離。作者討論對應方法，沒有給出適用所有投影片的固定字數、圖表數或停留秒數。[原始論文出版者頁](https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_6)、[原始論文全文鏡像](https://carpentries.github.io/instructor-training/files/papers/mayer-reduce-cognitive-load-2003.pdf)

同一論文的 segmenting 例子使用可由學習者點選繼續的短段落，且作者明示分段與互動仍需進一步拆解。這不能推出講者控制的現場演講應固定每頁 35 秒。論文也明示：沒有動畫時，口述與畫面文字一起呈現可能比只有口述更好；因此「觀眾在讀就不能聽」不是無條件成立的規則。[Mayer 與 Moreno，2003，pp. 47、49](https://carpentries.github.io/instructor-training/files/papers/mayer-reduce-cognitive-load-2003.pdf)

Mayer 與 Johnson（2008）進一步比較附有圖解與口述的短投影片；把 2–3 個關鍵詞放在對應圖解旁邊的條件，保留測驗較好，遷移測驗沒有優勢。研究支持的是特定形式的簡短標示，不能改寫成禁止任何重複文字，也不能把該實驗的 8–10 秒當成演講通用節奏。[原始論文 DOI](https://doi.org/10.1037/0022-0663.100.2.380)、[作者上傳的原始論文 PDF](https://www.researchgate.net/profile/Cheryl-Johnson-22/publication/232540768_Revising_the_Redundancy_Principle_in_Multimedia_Learning/links/631a4ff2071ea12e361ae26e/Revising-the-Redundancy-Principle-in-Multimedia-Learning.pdf?origin=publication_detail)

### coherence 看相關性，不是排除一切幽默

Mayer 撰寫、Cambridge 出版的章節摘要將 coherence 描述為移除無關內容；signaling 則是凸顯必要內容的組織。研究對象是多媒體學習，不是以娛樂為主要目的的舞臺表演。[作者章節摘要，2005 年紙本、2012 年上線](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/C98AB3A6CE760DD63C048936EA0B3B44)

產品推論：meme 若幫助建立正在說明的概念，不能僅因其幽默便判定無關；若只為固定頻率湊梗，可能與 coherence 目標衝突。本次來源沒有測試「每六頁一張 meme」的規則，不能稱為研究支持的預設值。

## 對原提案的辨識

下表的「未找到」僅限本次讀取來源，不代表整個研究領域沒有相關研究。

| 提案 | 證據判斷 | 對本專案需要釐清的界線 |
|---|---|---|
| `Style ≠ Theme` | 可作為領域區分。Microsoft 將 theme 說明為色彩、字型、背景／效果等視覺設定；它未把 theme 定義成論證與訊息安排。[Microsoft 官方說明](https://support.microsoft.com/en-us/powerpoint/create-your-own-theme-in-powerpoint) | 「樣式」是否只管視覺語法，或也管資訊分工與訊息安排，需要使用者決定；不能從這個區分自動擴張成敘事規劃工具。 |
| `max_concepts_per_slide: 1` | 訊息主張有方法脈絡，但「概念」不是同一個計量單位；一個主張可以依賴多個概念或比較項。 | 是一頁一個重點、論點、詞句，還是只能一個概念？需避免把不同單位混為同一門檻。 |
| `density: low/high` | 是產品描述，不能直接當作認知負荷測量。 | 應分辨文字量、物件量、論點量、圖表細節與版面占用；這些維度是分析建議，並非本次研究已驗證的單一密度公式。 |
| `seconds_per_slide: 35` | 本次來源未提供這個全域門檻的實證。 | 停留秒數是依內容與講述而變動的使用情境；若只交付風格處理，是否需要控制它尚未確定。 |
| `meme_frequency: 6` | 本次來源未測試這個值；單位與頻率定義也未寫清楚。 | 「允許幽默」與「強制每幾頁加梗」是不同產品行為。 |
| `handout_mode: false` | 可辨識資訊使用情境；本次來源未驗證這個布林參數。 | 推論：沒有講者補充的獨立閱讀，與有口述的投影，所需文字不同。可作為風格適用性條件，但不表示產品要製作講義或轉換檔案。 |
| 每頁依功能 `auto` 混搭 | 是 route 的設計假說；本次來源沒有比較四流派逐頁混搭與單一流派。 | 頁面功能如何判斷、風格是否可混用、全份一致性與人工覆寫，需要訪談；「更強」尚無證據。 |
| 多個 density / narrative / chart 參數可自由組合 | 是可調性提案，沒有各參數獨立成立的證據。 | 推論：若使用者把高橋流同時設定成高文字密度、密集圖表，可能改掉流派識別特徵；須釐清樣式身分與可覆寫程度。 |

需要避免的目標衝突：學習理解、舞臺情緒與事後獨立閱讀不是同一個成功指標；少字不必然等於少負荷；快速換頁與細讀證據可能衝突；人物風格識別與自由參數混搭可能衝突。這些是根據來源適用條件提出的需求分析，並不是四種風格的實驗比較結果。

## 公開開源 skill 的輕量查找

查找方法：以網頁搜尋限制 `site:github.com`，搭配 `SKILL.md` 和 `takahashi`、`takahashi method`、`slides`、`Steve Jobs`、`presentation`、`Bill Gates`、`忘形`、`wangxing`。搜尋索引不是完整 GitHub code search；未查核未公開套件，也未完成所有候選的授權與可執行驗證。

同一工作階段的主 agent 實際使用 Skills MCP search，回報下列結果：`Steve Jobs presentation`、`Bill Gates presentation`、`jobs`、`presentation style` 四個成功查詢，在 revision `67406af76bfe2b00170ae2b5724cd155cb8d5f5248876c2c2146789769380187` 回傳 `skills=[]`、`next_cursor=null`。`高橋`、`takahashi`、`忘形`、`wangxing` 四個查詢則回傳 `Internal error`；它們是查詢失敗，不能算作零結果。這只能證明該 revision、該服務與成功關鍵字的回應，不能覆蓋 GitHub 或其他 skill 平臺。

| 找到的原始檔 | 實際定位與限制 |
|---|---|
| [sethmblack/paks-skills — keynote-storytelling](https://github.com/sethmblack/paks-skills/blob/main/keynote-storytelling/SKILL.md) | 已讀 `SKILL.md`。檔案標示 MIT，明確以 Jobs 的產品發表敘事、投影片簡化等為題，另含演講結構與排練，超出本專案的純風格範圍。作者自行聲稱「proven」不構成研究驗證。可確認 Jobs 相關簡報 skill 存在，不能說所有現成 skills 都不存在。 |
| [alchaincyf/steve-jobs-skill — SKILL.md](https://github.com/alchaincyf/steve-jobs-skill/blob/main/SKILL.md) | 已讀檔案。名稱為 `steve-jobs-perspective`，是人物角色扮演與決策視角，並非專用投影片樣式；不應只依 repo 名稱判定符合需求。 |
| [wemamawe/ai-persona-skills — wangxing](https://github.com/wemamawe/ai-persona-skills/blob/main/wangxing/SKILL.md) | 搜尋結果可讀到 frontmatter：指的是美團創辦人王興，而非台灣簡報講者忘形。`wangxing` 有人物辨識碰撞，不能只以英文命中當成忘形流來源。 |

本次未辨識出直接對應高橋流、忘形流或比爾蓋茲流的專用樣式 `SKILL.md`。這是限定查找範圍的結果，不能推出它們不存在。也未找到符合「四個獨立樣式 skills＋一個 route skill、只管風格」的完整既有套件。

## 來源讀取狀況與限制

| 來源 | 本次實際讀取狀況 |
|---|---|
| Penn State 作者官方研究頁、assertion-evidence 官方首頁 | 已讀 HTML；其研究摘要可以支援方法與方向，本文未把官方倡議頁當成完整實驗資料。 |
| Garner 與 Alley，2013，官方 PDF | 搜尋索引讀到原文摘要；web 開啟重試失敗，terminal 下載另遇 DNS 解析失敗。未讀完整 PDF。 |
| Mayer 與 Moreno，2003 | 已讀原始論文 PDF 文字的相關段落（Carpentries 鏡像）；出版者搜尋結果核對題名、卷期、DOI。鏡像不是作者自有網站，但讀取的是原始論文。 |
| Mayer 章節，2005 | 已讀 Cambridge HTML 摘要；未讀需權限的完整章節。上線日期不應誤作紙本出版年。 |
| Mayer 與 Johnson，2008 | 已讀作者上傳原始 PDF 的摘要、方法脈絡與討論；APA DOI 頁工具無法開啟。不把作者上傳頁的文字視為後人整理。 |
| Microsoft theme | 已讀官方說明；它描述 PowerPoint 的產品概念，不證明本專案應如何定義全部「樣式」。 |
| GitHub 候選 skills | 兩個 Jobs 候選已開啟原始 `SKILL.md`；王興候選只讀搜尋結果。未安裝、執行或驗證技能效果，亦未固定到 commit SHA。 |
| Skills MCP search | 本研究子 agent 未自行呼叫；採用同一工作階段主 agent 提供的直接工具結果。revision 與成功／失敗查詢已逐一列出。 |

## 最值得帶回訪談的問題

1. 樣式 skill 能否更動頁面內容的資訊安排，還是僅描述文字、圖像、留白等視覺語法？
2. route skill 選擇的是整份、指定頁面或片段的樣式？混搭是否是本期需要，還是原提案的延伸假說？
3. 面對樣式與內容適用性衝突時，使用者希望保留流派特徵、保留原內容，或收到不適用的說明？
4. 風格驗收是「辨認得出這一派」、符合已列出的規則，還是要證明理解／說服效果？後者需要另一種證據，不能由檔案結構驗證替代。
