# Presentation style guidance — first release

## Problem Statement

Users and consuming agents need reusable presentation-style guidance with recognizable
differences between Takahashi, Steve Jobs, Wangxing (張忘形), and Bill Gates. A theme
or a list of vague adjectives does not explain those differences. Existing suggestions
also mix style with content planning, deck production, unsupported numerical presets,
and assumptions about a particular agent's tools.

The user wants four independently usable style skills and a route skill, designed
first for ChatGPT/GPT. The product must explain style constraints without taking over
content rewriting, restructuring, presentation production, or export.

## Solution

Deliver four focused style skills and one small route skill in the root product-skill
collection. Each style supplies source-led practical guidance, identifying core
features, adjustable aspects, relevant conditions, and exceptions. The route honors an
explicit choice, or selects one primary style from the context already supplied and
briefly explains the choice. It asks only when the selection lacks enough information.

Return complementary Markdown guidance and structured settings. Markdown explains
principles and their application boundaries; settings identify the style and carry
core and adjustable constraints. Shared rule identifiers connect the two. Settings
default to YAML and switch to JSON on an explicit request. Explanatory text follows
the user's language; identifiers and field names remain English.

First-release acceptance requires document checks and actual representative ChatGPT
trials. Skills MCP loading compatibility is a separately verified capability.

## User Stories

1. As a consuming agent, I want to load any of the four styles independently, so that
   I can obtain guidance when the desired style is already known.
2. As a user who names a style, I want the route to honor that choice, so that my
   preference controls the guidance I receive.
3. As a user without a style preference, I want a context-based choice with a concise
   reason, so that I can select an appropriate expression style without answering
   unnecessary questions.
4. As a user adjusting a style, I want compatible adjustments and an explanation of
   conflicting ones, so that the resulting guidance retains a recognizable identity.
5. As a consuming agent, I want complementary readable guidance and structured
   constraints, so that I can understand the conditions and reuse the settings.
6. As a user, I want source attribution and explicit evidence limits, so that project
   synthesis is not mistaken for an official method or an experimentally proven rule.
7. As a maintainer, I want document checks and recorded ChatGPT trials, so that a
   first-release usability claim is supported by the relevant surface.

## Implementation Decisions

### Product responsibilities and public seams

The agreed observable seams are:

- **S1 — Published guidance:** the product skill instructions, supporting rules,
  source records, and handoff contract that a consuming agent can read. This is the
  document surface approved by Q1, Q4–Q7, and Q13.
- **S2 — ChatGPT response:** the returned guidance and settings, selection or
  clarification, and adjustment/conflict explanation after an actual invocation.
  This is the response surface approved by Q2–Q3 and Q8–Q13.

These are document and response boundaries, not imagined functions, a new API, or a
presentation-generation engine. Actual transport through Skills MCP remains outside
the first-release acceptance gate. No product behavior currently exists; repository
structure checks are only prior art for document validation.

### Style content

Each style owns its guidance and can be used without invoking the route. Shared
principles may overlap, but each style must expose a distinguishing expression focus.
The following focuses are working project syntheses of the recorded sources, not
claims that the four creators published matching official specifications:

| Style | Distinguishing focus | Evidence boundary |
| --- | --- | --- |
| Takahashi | Words or phrases carry the primary visual focus through relative scale; supporting detail remains subordinate to that text focus. | Large text has direct publication support; phrase-level guidance is synthesis. Do not infer universal bans on charts or bullets from a text-first prototype. |
| Steve Jobs | A clear display, benefit, reveal, or comparison focus, supported by concise text and relevant visual evidence. | Recorded keynote excerpts support reveal and comparison observations; they do not establish a mandatory global storytelling sequence or universal layout formula. |
| Wangxing (張忘形) | A viewpoint becomes easy to grasp through concise text and a meaningful visual relationship, with audience relevance. | Creator descriptions support concise text/image communication; stories, humor, and black-and-white appearance are not universal requirements. The name refers to 張忘形, not 王興. |
| Bill Gates | Analytical expression makes evidence, quantities, comparisons, and system relationships interpretable through hierarchy and relevant annotations. | The analytical orientation has first-person support. The resulting style rules are project synthesis, not a formal “Gates method”; high density is not mandatory. |

Detailed rules must preserve these distinctions and the recorded evidence boundaries.
Rules may describe expression preferences across related material; they must not
execute rewriting, split or merge pages, invent an outline, or arrange a speaking
itinerary. Examples explain rules rather than transform the user's content.
This boundary applies to the style skills' responsibilities; it must not prohibit
separately authorized work by a consuming agent or tool that uses the guidance.

The following mandatory core records make the identifying relationships observable.
These are project rule identifiers and synthesis, not quotations or official names.
Every completed profile includes its style's mandatory record, and Markdown states
the same propositions. A color, font, or generic preference alone does not satisfy it.

| Mandatory rule ID | Required propositions | Compatible boundary example | Conflicting boundary example |
| --- | --- | --- | --- |
| `takahashi.text_primary` | Words/phrases are the primary visual/message carrier. Relative scale establishes that priority. Other detail, if included, is supporting rather than an equal or dominant focal point. | Permit a chart and three lines of auxiliary notes while explicitly keeping them subordinate to the primary words/phrases. | Make a dense chart or prose paragraph the primary carrier, with the words/phrases relegated to a minor heading. |
| `jobs.single_focus` | Display, benefit, reveal, or comparison elements support one stated focal point. Text/visual elements have a supporting relationship to that point rather than independent competing claims. | Change colors or include several objects that serve the same comparison point. | Give several unrelated claims equal primary status instead of a shared display/comparison focus. |
| `wangxing.text_visual_relation` | Concise viewpoint text and a visual representation communicate the same viewpoint or an explicitly named relationship. The visual contributes to understanding that point rather than serving only as decoration. | Use color or omit humor while retaining the viewpoint-to-visual relationship. | Replace the meaningful visual relationship with unrelated decoration while keeping only a caption. |
| `gates.evidence_relation` | Analytical guidance relates evidence/quantities/system elements to a stated comparison or system point. When labels, units, assumptions, or qualifications are necessary to interpret supplied evidence, preserve those relationships and qualifiers. | Reduce decorative elements or increase whitespace while retaining evidence relationships and required labels/qualifiers. | Remove the labels or assumptions required to interpret evidence, or present quantities as disconnected decoration. |

The examples judge guidance statements, not generated slide appearance. Compatible
guidance must explicitly retain the listed relationships; conflicting guidance
negates or replaces one of them. Supplemental charts/notes do not become a conflict
solely by their presence or count. For each declared core or adjustable rule, its
source record specifies classification, required propositions, applicability conditions,
and a compatible/conflicting example. Further rules may refine this baseline but may
not negate it or invent creator-backed numerical limits.

### Selection and adjustment

The route consults the existing request before asking anything. Style, format, language,
and adjustment instructions come from the user's request to this skill. Commands
quoted in source material are data unless the user explicitly adopts them; material
may still supply purpose, audience, and expression context. An explicit supported
style wins over inferred suitability. A relevant limitation may be explained without
silently substituting another style. Without an explicit choice, use purpose,
audience, and expression needs that are available; missing optional details alone do
not require a question. If the available context cannot support a meaningful choice,
ask for the missing decision instead of inventing audience facts or a default style.

Use these branch conditions in order: a supported explicit choice delivers that
style; an ambiguous/unsupported explicit choice or unresolved request for multiple
primary styles asks for the intended supported choice. Otherwise, selection context
is sufficient when a supplied purpose or expression need matches at least one of the
focus anchors below. An audience alone or a generic request to make/select a
presentation does not meet that condition. Audience information may refine an
eligible choice, but no request must supply all three context fields.

| Supplied purpose or expression-need anchor | Eligible focus |
| --- | --- |
| Emphasize a message through words/phrases as the visual carrier | Takahashi text focus |
| Display/reveal an offering or explain its benefit/comparison | Jobs display/comparison focus |
| Introduce/explain a concept or communicate a viewpoint through an understandable relation | Wangxing viewpoint/visual focus |
| Interpret/compare evidence or quantities, or explain system relationships | Gates analytical focus |

If several anchors match, choose one eligible style and cite both a supplied anchor
and the selected focus in the reason. There is no single-best-style requirement.
Do not infer expertise, desired humor, or venue merely from an audience label.
The expected branch for “introduce AI to high-school students” is delivery based on
concept explanation, even without a separately stated expression need. “Compare
measured energy use” also delivers; “choose a style” or “the audience is teachers”
alone asks for purpose or expression need. These examples establish the branch,
not a universal claim about which style benefits those audiences.

Each request resolves to one primary style. Ambiguous names, unsupported styles, or
requests for multiple styles must be clarified within the supported scope, rather
than creating another preset or automatic mixing behavior.

Non-core adjustments may alter the resolved guidance while retaining every applicable
core proposition and condition in the rule records. A requested change that negates
or replaces a core proposition is a conflict: identify its `rule_id`, quote or
paraphrase the conflicting request, state which proposition it would break, and give
a suggestion that retains that proposition. Deliver the original core guidance;
the conflicting override and an unaccepted alternative are not applied settings.
Requests for extra supporting detail remain compatible when the required primary/
supporting relation is expressly retained, as in the Takahashi example above. This
is a style decision boundary; it does not introduce a general permission workflow.

### Minimal handoff contract

Both standalone and routed guidance use the same semantic contract:

- `style_id` identifies one of `takahashi`, `jobs`, `wangxing`, or `gates`. These are
  project identifiers; `wangxing` is not claimed as the creator's official English name.
- `core_rules` is a list of records containing a nonempty English `rule_id` and a
  nonempty explanatory `constraint` string.
- `adjustable_rules` is a list of records with the same two fields, representing the
  applicable non-core guidance after compatible adjustments; it may be empty when
  no such rule applies.

Rule identifiers are unique within a profile, identify the same rule in Markdown and
settings, and retain their identity across language and serialization changes.
The mandatory IDs in the core-record table are fixed; other published rule IDs are
looked up in their source records rather than regenerated from wording.
The settings describe style constraints; they are not executable commands, a slide
plan, or a deck document model. A constraint must retain any condition needed to
interpret it correctly. Markdown supplies the explanation and relevant exceptions;
the two representations are complementary rather than complete copies.

Use the published rule records as the semantic comparison oracle. For every core
rule, include all required propositions and applicability conditions in both Markdown
and its settings `constraint`; retain a conditional rule as a conditional instruction
even when the request supplies no facts to resolve it. For an included adjustable
rule, retain its applicable propositions, conditions, and accepted changes in both.
Reasons, historical background, and illustrative examples may remain Markdown-only;
conditions that limit when a constraint applies may not. For example, a rule restricted
to spoken projection cannot be serialized simply as “use short text” without that
restriction. An independent-reading exception that changes the instruction must
appear in the constraint as well as Markdown.

The comparison checklist for each returned `rule_id` is: correct classification;
each required proposition present; each applicability restriction retained; no
contradictory proposition; no unaccepted adjustment. Every mandatory core ID must
be present. Direct/routed, YAML/JSON, and language variants are judged against that
same checklist and catalog, not against each other's exact words. Paraphrase,
translation, ordering, and explanatory examples may vary; changing the subject,
primary/supporting relation, conditional scope, or force of a required proposition
fails the checklist. The approved test plan records the expected propositions and
conditions for each case before trials begin, using this baseline and source records.

Use only JSON-compatible data types in the YAML representation, without custom tags
or host-specific objects. An explicit JSON request changes serialization, not the
schema or rule meaning. Emit Markdown plus exactly one structured representation
when delivering guidance. A clarification that cannot yet select a style need not
fabricate a profile.

### Discovery and host boundary

Descriptions distinguish style selection from the use of a named style. Keep the
route small; resolve the selected style and read its guidance, with supporting
evidence or examples read as needed. Do not require every invocation to read all four
styles or all research notes. Do not assume that ChatGPT has a shell, local file
paths, Codex/Claude commands, or an available MCP connection. If the chosen guidance
cannot be accessed, report that limitation rather than fabricate loaded rules.

OpenAI's GPT-6 Astra article informs concise descriptions, progressive disclosure,
and clear completion boundaries. Its Codex-specific behavior is not proof of a
ChatGPT or Skills MCP loader contract. The product is not restricted to Astra.

### Acceptance criteria

| ID | Observable requirement |
| --- | --- |
| AC-01 | The published product contains four styles corresponding to the four agreed identities and one route, separate from development collaboration skills. |
| AC-02 | Style instructions and delivered responses provide guidance and constraints; they do not perform content rewriting, reordering, page splitting/merging, production, rehearsal, or export. |
| AC-03 | Each style declares the mandatory core record and all its propositions from the core-record table, plus classifications, conditions, and compatible/conflicting examples for its rules. Guidance that substitutes color/theme or generic simplicity for the mandatory relationship fails. |
| AC-04 | Style rules distinguish direct source support, sample observations, and project synthesis. Each identifying core rule has a traceable source or explicitly labeled inference with its basis; evidence limits are retained. |
| AC-05 | Direct style use returns its guidance without requiring the route. For matching context and adjustments, routed use of that style preserves the same identity and rule meaning. |
| AC-06 | An explicit supported choice is honored even if another style might be recommended from context; optional missing context does not prevent delivery. |
| AC-07 | Without an explicit choice, a supplied purpose/expression need matching a focus anchor produces one eligible style and a reason citing the supplied anchor and chosen focus, without asking for additional selection context. |
| AC-08 | A request with no supported explicit choice and no focus anchor, or an ambiguous/unsupported explicit choice, asks for purpose/expression need or an intended supported style respectively; it does not invent a preference, audience fact, or profile. |
| AC-09 | A completed response contains one primary style. A multi-style request is clarified rather than implemented as local mixing or automatic per-page routing. |
| AC-10 | A non-core adjustment that retains every applicable core proposition/condition is reflected in Markdown and settings, with those propositions/conditions retained. The published compatible boundary cases are treated as compatible. |
| AC-11 | A request negating/replacing a core proposition receives its rule ID, the conflicting request, the broken proposition, and a suggestion retaining it; delivered settings keep the core and do not apply the conflicting override or an unaccepted alternative. |
| AC-12 | Completed guidance includes Markdown and one profile with the supported style ID, every mandatory core record, and included adjustable records. Both include each record's required propositions and scope-changing conditions; background, reasons, and examples may remain Markdown-only. |
| AC-13 | Default settings are parseable YAML. An explicit JSON request produces parseable JSON with the same contract and meaning. Each completed response emits only one structured format. |
| AC-14 | Required fields/types and mandatory core IDs are present, IDs are unique within the profile and stable for the same catalog rule across language/serialization. Every returned rule passes the semantic comparison checklist in both representations and direct/routed use. |
| AC-15 | All user-visible explanations, including clarification and availability reports, and constraint text follow the requested language or the user's conversation language; Chinese uses Taiwan Traditional Chinese. Field names, style identifiers, and rule identifiers remain English. |
| AC-16 | Descriptions and load instructions distinguish the five skills, allow direct use and routing, and use supporting material on demand without assuming local tools or an installed MCP connection. Unavailable guidance is reported without fabrication. |
| AC-17 | Document checks cover completeness, source attribution, style distinction, rule references, scope, and handoff consistency. Passing repository plumbing alone is insufficient for first-release acceptance. |
| AC-18 | Actual ChatGPT trials cover all four styles, direct/routed use, selection and core-boundary examples, scope-changing conditions, quoted-command separation, default YAML/requested JSON, and Chinese/English output. Results include the request, supplied skill revision/content, observed response, host/model information available, and criterion outcome. |
| AC-19 | Release evidence distinguishes document checks, actual ChatGPT trials, and Skills MCP loading; untested MCP compatibility is explicitly marked unverified and does not block the agreed first-release gate. |
| AC-20 | Fixed word counts, slide timing, meme frequency, or density thresholds are not attributed to creators or research without supporting evidence. Project choices and context-specific suggestions are identified as such. |

## Testing Decisions

Test external behavior at S1 and S2. Evaluate rule meaning, selection, evidence
boundaries, and compatibility with the request, not exact prose, paragraph order,
hidden reasoning, or an assumed internal tool sequence. The traceability matrix
defines the applicable type/field/boundary combinations for these criteria.

- **Document surface:** check the five product definitions, independent entry points,
  source/rule attribution, distinguishability, consistent identifiers, JSON-compatible
  YAML and equivalent JSON examples, and the pure-style scope. Use document review
  where semantic interpretation is required rather than reducing it to keyword matches.
- **ChatGPT surface:** conduct actual trials with the product instructions supplied
  through a method available in that host and record what was supplied. Cover the
  conditions in AC-18 using representative cases; criteria can share a case. Compare
  responses with the declared style rules, not a presumed empirical learning benefit.
- **Equivalent output:** compare parsed settings and shared rule meanings under the
  same request with only serialization changed, using the rule-record checklist and
  stable identifiers. Include the scope-changing condition case and boundary examples
  above. Do not require identical translated wording or identical nondeterministic outputs.
- **Evidence discipline:** distinguish a document pass, local/subagent simulation,
  actual ChatGPT trial, and MCP loading trial. Simulation cannot replace AC-18.
  No acceptance outcome is currently claimed.

The repository's portable verifier is prior art for static structure checks only;
there is no existing product test suite or behavior harness. Before writing ticket
tests, propose the cases and means of recording the actual surface in the required
test plan table and obtain approval. These testing decisions do not constitute that
approval. A model/version change limits the scope of previously recorded trial evidence;
do not generalize a pass to all GPT models or future host versions.

The approved plan fixes cases, expected branches/propositions, executions, and retry
policy before trials. Retain every observation, including failures and reruns, with
its request, revision, and verdict. A case passes only if all its required checks pass
in every execution counted by that plan; an observed failure for that revision is
not erased by a successful retry. After correction, record a new revision and its
results separately. A criterion passes only when every case assigned to it passes;
an unexecuted check is unverified, not a pass. First-release acceptance requires all
AC-01–AC-20 to pass at their declared surfaces; AC-19 may pass with MCP explicitly
unverified. This is a claim about recorded trials, not a universal success-rate claim.

## Out of Scope

- Content rewriting, outline planning, new research arguments, page restructuring,
  slide generation, speaker notes, rehearsal, production workflows, and file export.
- Local style exceptions, multiple primary styles, and automatic per-page mixing.
- MCP server development, publication, account connections, or mandatory MCP loading
  certification in this first release.
- Guaranteed compatibility with all GPT models, Codex, Claude Code, or presentation tools.
- Historical deck replication, mandatory persona roleplay, or claiming author endorsement.
- Empirical claims of superior learning, persuasion, or performance across the four styles.

## Further Notes

The requirements come from Q1–Q14 and the confirmed Charter. See the
[decision record](../../docs/research/2026-10-03-style-design-context.md),
[Takahashi/Jobs source boundaries](../../docs/research/2026-10-03-takahashi-jobs.md),
[Wangxing/Gates source boundaries](../../docs/research/2026-10-03-wangxing-gates.md),
and [cross-style evidence boundaries](../../docs/research/2026-10-03-style-boundaries.md).
The companion [traceability matrix](traceability.md) is the coverage source for
the acceptance criteria.

The user-requested
[OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
was read during discovery. Source notes record the actual reading scope and limitations;
unread book contents and unmeasured slide visuals must not become supporting evidence.

This is an unfrozen stage-2 spec, created on 2026-10-03. It does not authorize tickets,
tests, implementation, or a release. The Chinese audit translation is produced after
adversarial review passes and records the English source hash, as required by the
project's language convention. The first implementation has no established product
seams; the walking-skeleton rule remains applicable. This specification records the
approved first-release behavior, without claiming a skeleton has already landed or
that its exemption waives later review requirements.
