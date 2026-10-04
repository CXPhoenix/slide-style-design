# 高橋流與賈伯斯流：來源、原始脈絡與風格邊界

查閱日期：2026-10-03（Asia/Taipei）。本筆記為需求訪談的研究材料，不是 spec、技能實作或已核准的產品規則。

本專案已確定提供數個樣式 skills 與一個 route skill，產品 skills 放在 `skills/`；僅處理風格。以下刻意區分「原創者明示的方法」「演講樣本的觀察」「本專案可能採用的設計推論」。

## 來源與實際閱讀範圍

| 代號 | 來源與品質 | 已讀內容 | 限制 |
| --- | --- | --- | --- |
| T1 | [SB Creative：高橋征義《でかいプレゼン 高橋メソッドの本》](https://www.sbcr.jp/product/4797332530/)，原書出版社的一手出版資料 | 作者、2005-11-29 出版日期、書籍介紹 | 未讀完整原書；出版社介紹不能代表全書所有規則 |
| T2 | [高橋征義：LTを支える技術（LLD'11 Winter）](https://www.slideshare.net/takahashim/ldd11-w)，本人帳號上傳的演講材料 | 144 頁投影片的網頁文字／圖像替代文字；作者自介、重點與刪減、關係模型、條列等範例 | 未下載 PDF，未逐頁視覺量測，未聽演講；它是本人後期 LT 演講，不等於最初方法的完整定義 |
| J1 | [Steve Jobs Archive：Make Something Wonderful](https://book.stevejobsarchive.com/)，家屬成立的典藏機構出版、保存本人言論 | 2007 Macworld 的 iPhone 發表節錄，以及括號中的舞台／圖像說明 | 書中為節錄；不涵蓋整場 demo、recap 或每頁視覺細節。機構背景另見 [About the Archive](https://stevejobsarchive.com/about) |
| J2 | [Apple Events：Macworld San Francisco 2007 Keynote Address](https://podcasts.apple.com/ca/podcast/macworld-san-francisco-2007-keynote-address/id1473854035?i=1000756334348)，Apple 官方影片入口 | 節目中繼資料、日期、講者與介紹 | 未完整播放；不能據此聲稱已量測頁數、字數、留白比例、照片頻率或每頁秒數 |
| J3 | [Apple：Apple Presents iPod](https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/)，2001-10-23 官方發表新聞稿 | 標題、規格、Jobs 引言與容量／傳輸速度表述 | 證明官方如何表達產品效益與數字，不是原始投影片版面證據 |
| J4 | [Stanford：2005 年 Jobs 畢業演講備稿](https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says)，演講主辦單位公布本人講稿 | 三段人生故事與結尾 | 是演說而非產品發表簡報；支持 Jobs 的故事表達能力，不能直接轉成投影片規格 |
| J5 | [Steve Jobs Archive：The Objects of Our Life](https://stevejobsarchive.com/stories/objects-of-our-life)，原始影片典藏與策展說明 | 1983 Aspen 演講的策展文字、原始影片入口與材料脈絡 | 未完整播放影片；策展者的描述要與本人逐字發言分開 |

原始高橋流網站 [rubycolor.org/takahashi](https://www.rubycolor.org/takahashi/) 與 [最初介紹投影片入口](https://www.rubycolor.org/takahashi/takahashi/img0.html) 本次未能讀取；網頁工具回傳錯誤，終端嘗試則無法解析 hostname。這是本次存取限制，不能斷言網站已永久消失。搜尋中見到第三方重製與 Wikipedia，僅用來找回來源，未把它們當成原創者的規則依據。

## 高橋流：可核對之處

出版社明確把「非常大的文字」列為高橋方法的特色，且原書由創作者本人撰寫、重現他用同一方法介紹方法的投影片。這個名稱有可追溯的原創者與自述材料。[T1](https://www.sbcr.jp/product/4797332530/)

本人後期材料以短詞逐頁推進，也明示引起注意、讓人記得、刪減主題及保留值得說的內容；網頁擷取文字顯示第 4 頁有自介條列，第 18–19 頁有傳達關係模型。這證明「本人所有簡報都絕不出現圖／條列」過度概括，但不能反向證明原始純文字方法允許任意圖表。[T2](https://www.slideshare.net/takahashim/ldd11-w)

| 使用者素材中的說法 | 本次識別 |
| --- | --- |
| 超大字、極少字 | 超大字有創作者原書出版社的直接依據；短詞／低資訊密度有本人樣本支持。不能直接推出固定 font size 或中文字數上限。[T1](https://www.sbcr.jp/product/4797332530/)、[T2](https://www.slideshare.net/takahashim/ldd11-w) |
| 一頁一個訊息 | 可作本專案的操作性偏好，但一頁可能只是詞、連接語或某句的一部分；不必每頁都是獨立完整論點。這是對樣本的歸納。[T2](https://www.slideshare.net/takahashim/ldd11-w) |
| 快速換頁 | 樣本有短片段連續推進，但沒有本次已讀的原創者時間量測。固定每頁 5 秒或 35 秒不應當成歷史定義。 |
| 幾乎不依賴 bullet／chart | 適合作低密度傾向；「純文字原型」與「創作者後期實踐」需要分開，不能偷偷把傾向升級成跨情境禁令。 |

## 賈伯斯流：觀察可以成立，普遍公式仍需證據

2007 iPhone 節錄具有重複鋪陳、三項產品合一的揭露，也用二軸圖與四款既有手機比較。這支持用少量可辨認元素形成一個比較焦點；它不支持「每頁只能有一個物件」或「完全不用圖表」。這是從本人演講歸納，並非 Jobs 親自發布的通用風格規範。[J1](https://book.stevejobsarchive.com/)

2001 iPod 官方文案把 5 GB 換成可攜帶 1,000 首歌的用途，也交代相對體積與傳輸速度。數字可連結可理解的效益；但新聞稿不能證明投影片一定使用視覺化比較或禁止表格。[J3](https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/)

Stanford 的三段故事與 Aspen 的筆記／問答脈絡提醒我們：Jobs 的表達會依場合改變，不能把產品發表的一種排列當成所有演講的固定公式。[J4](https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says)、[J5](https://stevejobsarchive.com/stories/objects-of-our-life)

| 使用者素材中的說法 | 本次識別 |
| --- | --- |
| 強敘事弧線 | 原始演講可支持「具敘事／揭露技巧」；改寫整份簡報的故事弧仍是另一項能力。[J1](https://book.stevejobsarchive.com/)、[J4](https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says) |
| 一頁一個主張 | 可作設計偏好；不要把一個比較主張拆成不能同時比較的零碎頁。本次未逐頁核對所有 Jobs 投影片。 |
| 大量產品圖、照片、短句，留白極大 | 尚未完成原始影片的逐頁視覺核對；本次不給比例、頻率或通用硬限制。官方影片入口可供後續抽樣。[J2](https://podcasts.apple.com/ca/podcast/macworld-san-francisco-2007-keynote-address/id1473854035?i=1000756334348) |
| buildup → reveal → demo → recap | 有 buildup／reveal 的原始片段；本次節錄不能證明完整鏈，更不能聲稱是 Jobs 的唯一方法。[J1](https://book.stevejobsarchive.com/) |
| 數字用視覺化比較而非塞滿表格 | 有效益表達與比較原例；「不塞滿」可以是本專案偏好，「數字一律不得用表格」缺乏本次直接依據。[J1](https://book.stevejobsarchive.com/)、[J3](https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/) |

## 可供純風格 skills 訪談的候選規則

以下是設計推論，尚未核准；不是歷史人物的原話，也不是要求現在開始實作。

1. **高橋流可用「文字承載主要視覺焦點」識別。** 檢視的是相對尺度、詞句精煉與閱讀焦點；若為了放大而刪掉重要限定條件，應回報衝突。
2. **賈伯斯流可用「一個清楚的展示／比較焦點」識別。** 圖像、短句或少量比較物件共同支援焦點；四物件可能服務同一主張，不因物件數而自動失敗。
3. **低密度是風格選擇，資料真實性不是可犧牲的參數。** 當目前內容需要精確比較、完整程式碼或不可刪的註記，route skill 可以識別不合適之處；不能靠刪除證據達成外觀。
4. **來源忠實程度應可說明。** 若加入圖表、照片或多層資訊，可以說是高橋流啟發的延伸；不需宣稱與原始方法完全相同。
5. **先用相對／語意限制，暫不硬化秒數、字數與元素數。** 任何定量 preset 都應列為本專案自訂值，另有使用情境與例外，不能用名人名稱替它背書。

上述推論分別由 T1／T2 的文字焦點、J1 的比較原例、J3 的效益表達啟發；可追溯來源不等於已證明其對所有受眾有效。[T1](https://www.sbcr.jp/product/4797332530/)、[T2](https://www.slideshare.net/takahashim/ldd11-w)、[J1](https://book.stevejobsarchive.com/)、[J3](https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/)

## 避免跨入製作流程

| 可以繼續訪談的風格處理 | 涉及內容規劃或製作、需另外界定的行為 |
| --- | --- |
| 既有內容的文字大小、資訊層級、相對密度與視覺焦點 | 自行決定演講目標、研究論證、資料來源與整份大綱 |
| 既定頁面／區塊的展示、比較、文字焦點等表達偏好 | 自行拆頁、增刪頁數、重排整份簡報、撰寫講稿 |
| 對既有揭露需求描述視覺表現偏好 | 安排 buildup／reveal／demo／recap 的全局發表流程 |
| 說明 route 選擇與風格衝突，交由呼叫方決定內容處理 | 接管 rehearsal、配秒、現場 demo、製作／匯出 PPTX 或 Google Slides |

原稿的 `narrative planner` 若負責自行建立目標、大綱與發表流程，尚無使用者授權將這些工作納入產品。既有內容的摘寫、拆頁、重排是否屬於使用者所指的風格，則仍需第一輪訪談界定，不能由研究者先行排除或納入。`slide-role classifier` 也只能先當候選名稱：接受既有頁面功能與自行創作頁面功能，責任不同。這是需求邊界辨識，不是外部來源替專案下的決定。

## 下一輪訪談待識別事項

- 「風格」是否允許改寫既有句子，或只提供規則？允許縮句時，如何保留限定條件？
- route skill 接收使用者明選的風格，還是可自動建議？自動模式的輸入是整份既有內容、單頁內容，或已標註角色的區塊？
- 混用風格是否需要整份共用的字體、色彩與圖表語言，還是允許不同頁有完整不同外觀？這是尚未決定的產品選擇。
- 名稱要表達原始方法的忠實實作，或以人物啟發的設計傾向？這會影響規則嚴格程度與例外說明。

本次沒有做資訊保留率、可讀性或教學成效實驗；原始樣本也不能單獨證明某風格適合所有教師、研究者或技術受眾。
