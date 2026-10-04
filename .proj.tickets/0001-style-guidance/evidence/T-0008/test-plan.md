# T-0008 test plan

User approved continuous T-0005–T-0014 plans and assistant-operated ChatGPT trials on 2026-10-04. Existing public document/settings and real conversation seams; one serialization objective only. Written before tests.

| Slice | Public seam | Expected check | Evidence | Boundary / scoped AC |
|---|---|---|---|---|
| 1 | Published JSON examples across four styles | Parse same three fields, types, IDs, core/accepted preferences as paired YAML; all scope conditions retained | One bounded catalog test, red/green; semantic review | S1; explicit JSON vs default YAML; AC-12/13/14/18/19 |
| 2 | Actual ChatGPT default / explicit JSON | Markdown plus only requested serialization; same catalog propositions, independent-reading exception, team qualifier, accepted preferences | CT-01/02 full response, hashes and screenshots | S2; independent reading/team restriction/accepted preferences; AC-05/12/13/14/18/19 |

Catalog checklist: Takahashi text priority/relative scale/subordinate detail; Jobs stated single focus/supporting elements; Wangxing concise viewpoint/meaningful visual contribution and independent-reading condition; Gates evidence-to-stated-analysis and necessary units/assumptions/qualifiers. Preferences retain each core. Inspect all four paired examples semantically; static equality does not prove generated model behavior.

CT-01 default YAML:
> 請使用忘形流，提供自行閱讀社群圖文的風格指引與設定。接受彩色、不使用幽默；保留「在這個團隊中，清楚分工有助減少重複工作」，視覺是任務區塊對應各人的分工。不依賴講者補充。只提供風格約束，不改寫或重組素材。用台灣繁體中文回答。

CT-02 explicit JSON, same material:
> 請使用忘形流，提供自行閱讀社群圖文的風格指引與設定，設定明確要求 JSON。接受彩色、不使用幽默；保留「在這個團隊中，清楚分工有助減少重複工作」，視覺是任務區塊對應各人的分工。不依賴講者補充。只提供風格約束，不改寫或重組素材。用台灣繁體中文回答。

One run per case/candidate. Preserve failed outputs; fix a new candidate and rerun affected cases. One retry for technical interruption only. Skills MCP remains unverified.
