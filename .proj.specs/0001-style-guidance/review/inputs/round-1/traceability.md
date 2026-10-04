# First-release style guidance traceability

Created: 2026-10-03. Source: confirmed Q1–Q14 and Project Charter.
Companion: [English specification](spec.en.md).

S1 is the published guidance/document surface; S2 is an actual ChatGPT response.
These reuse the agreed document and response boundaries. Rows are applicable
combinations of type × field × boundary, not every mathematically possible pairing.
An acceptance reference is a requirement, not a test result.

| Row | Type | Field / concern | Boundary and representative condition | Expected behavior | Acceptance criterion | Decision / evidence basis |
| --- | --- | --- | --- | --- | --- | --- |
| TR-01 | Product collection | Composition / location | S1: product skills versus development skills | Four styles and one route in root `skills/`; development skills remain in their runtime trees. | AC-01 | Q4; user product-location instruction |
| TR-02 | All styles and route | Responsibility | S1/S2: request includes existing content or a production request | Deliver style guidance; content transformation and production remain with the consuming tools. | AC-02 | Q1; Charter |
| TR-03 | Takahashi | Core focus / conditions | S1/S2: text-led expression | Text provides the primary focus, with relative scale and compact phrasing; conditions distinguish prototype and later observations. | AC-03, AC-04 | Q5/Q7; T1/T2 in Takahashi/Jobs research |
| TR-04 | Steve Jobs | Core focus / conditions | S1/S2: display, reveal, benefit, or comparison expression | Guidance explains a clear display/comparison focus; no mandatory whole-deck narrative or invented visual metrics. | AC-03, AC-04 | Q5/Q7; J1/J3 in Takahashi/Jobs research |
| TR-05 | Wangxing | Core focus / identity | S1/S2: concise visual explanation | A viewpoint is conveyed through concise text and meaningful visual relationships; refers to 張忘形, without mandatory memes or oral-only usage. | AC-03, AC-04 | Q5/Q7; W1/W2/W4/W6/W7 in Wangxing/Gates research |
| TR-06 | Bill Gates | Core focus / evidence status | S1/S2: analytical expression | Explain evidence/quantity/system relationships; identify project synthesis without asserting an official method or mandatory high density. | AC-03, AC-04 | Q5; G1/G3 in Wangxing/Gates research |
| TR-07 | All styles | Distinction | S1: compare all four definitions | Identifying expression differences are documented beyond label, background, font, or generic “simple” wording; shared principles may overlap. | AC-03 | Q4/Q5/Q13; research synthesis |
| TR-08 | All styles | Attribution | S1: identifying rules and source records | Core rules trace to direct statements, observations, or labeled inference with its basis and reading limitations. | AC-04 | Q5; all source notes |
| TR-09 | Direct style use | Entry point | S1/S2: each named style used without route | Each of the four styles independently delivers its own guidance and the common handoff contract. | AC-05, AC-12 | Q6/Q9/Q10 |
| TR-10 | Routed style use | Rule meaning | S2: same style/context/adjustments as direct invocation | Route preserves that style's identity and meaning; it does not carry a divergent second rule set. | AC-05 | Q6/Q10 |
| TR-11 | Route | Explicit selection | S2: supported style named, with contrary inferred suitability | Honor the explicit choice; mention relevant limitations without substituting another style. | AC-06 | Q2 |
| TR-12 | Route | Optional context | S2: supported style named without audience/purpose details | Deliver named guidance without requiring unnecessary selection questions. | AC-06 | Q2 |
| TR-13 | Route | Contextual selection | S2: style absent, meaningful purpose/audience/expression context supplied | Select one style and give a concise context-based reason. | AC-07, AC-09 | Q2/Q3 |
| TR-14 | Route | Insufficient context | S2: style absent and no meaningful selection basis | Ask a focused clarification; do not invent facts or fabricate a profile. | AC-08 | Q2 |
| TR-15 | Route | Ambiguous / unsupported choice | S2: name does not identify one supported style | Clarify the intended supported choice rather than invent another preset. | AC-08, AC-09 | Q2/Q3/Q4; bounded selection implication |
| TR-16 | Route | Multiple choices | S2: user requests mixed styles or per-page auto routing | Clarify one primary style; do not perform deferred mixing behavior. | AC-09 | Q3 |
| TR-17 | All styles | Compatible adjustment | S2: requested non-core change preserves identity | Reflect the change in applicable guidance and settings; retain core meaning and identifiers. | AC-10, AC-14 | Q7/Q10 |
| TR-18 | All styles | Conflicting adjustment | S2: requested change undermines core identity | Explain the conflict and offer a compatible suggestion without silently applying the override or an unaccepted suggestion. | AC-11, AC-14 | Q7 |
| TR-19 | Completed guidance | Markdown | S2: selected style can be delivered | Explain principles, relevant conditions and exceptions, and the reason/conflict when applicable. | AC-12 | Q2/Q7/Q9/Q10 |
| TR-20 | Completed guidance | Structured contract | S1/S2: profile is delivered | `style_id` is a supported English identifier; core and adjustable rule lists contain nonempty `rule_id` and `constraint` records; an applicable adjustable list may be empty. | AC-12, AC-14 | Q9/Q10; minimal contract synthesis |
| TR-21 | Completed guidance | Default serialization | S2: no JSON request | Emit Markdown and exactly one parseable YAML profile with JSON-compatible types. | AC-13 | Q11 |
| TR-22 | Completed guidance | Requested serialization | S2: explicit JSON request | Emit Markdown and exactly one parseable JSON profile; preserve the YAML contract's fields, types, and meaning. | AC-13, AC-14 | Q11 |
| TR-23 | Completed guidance | Rule references / conditions | S1/S2: compare settings with associated Markdown | IDs are unique within the profile, refer to the same rules, and preserve essential conditions without contradictory guidance. | AC-14 | Q10 |
| TR-24 | Completed guidance | Chinese / English explanations | S2: Chinese and English requests or explicit output-language instruction | Follow the requested/user language; Chinese uses Taiwan Traditional Chinese, while all field and rule identifiers stay English. | AC-15 | Q12; project language rule |
| TR-25 | Product instructions | Discovery / disclosure | S1: named style versus route, relevant references | Distinguish triggers; read selected guidance and supporting material as needed, without loading all styles/research by default. | AC-16 | Q6/Q8; OpenAI article design synthesis |
| TR-26 | Product instructions | Host / availability boundary | S1/S2: ChatGPT has no shell/local paths/MCP, or selected guidance cannot be accessed | Guidance makes no local-tool assumptions; inaccessible rules are reported without pretending they were loaded. | AC-16 | Q8; host-boundary implication |
| TR-27 | Product validation | Document evidence | S1: release readiness review | Inspect all five skills, attribution, distinguishing rules, scope, references, and handoff consistency; static plumbing does not establish model behavior. | AC-17 | Q13 |
| TR-28 | Product validation | Actual ChatGPT evidence | S2: representative acceptance trials | Record actual inputs, supplied skill content/revision, response, available host/model information, and outcomes across the required cases. | AC-18 | Q8/Q13 |
| TR-29 | Compatibility statement | MCP status | S1: first-release evidence with no loading trial | Mark Skills MCP loading unverified separately; do not replace actual ChatGPT trials with local or MCP-adjacent evidence. | AC-19 | Q8/Q13 |
| TR-30 | All styles | Quantitative / historical claims | S1/S2: word limits, timing, humor frequency, density, creator attribution | Do not label unsupported presets or generalizations as creator/research rules; identify project choices and conditions. | AC-20, AC-04 | Q5; style-boundaries research |

Every AC-01–AC-20 is reached by at least one row. No trial has been conducted against
product skills yet; the table records intended coverage, not a coverage report.
The formal implementation test plan remains subject to the project's separate approval gate.
