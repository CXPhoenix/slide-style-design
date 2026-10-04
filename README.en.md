# Slide Style Design

**English** · [繁體中文（台灣）](README.md)

![Slide Style Design — Four styles. One clear direction.](docs/assets/banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 4 styles + 1 route](https://img.shields.io/badge/Skills-4_styles_%2B_1_route-167D8D.svg)](skills/)
[![Output: Markdown + YAML / JSON](https://img.shields.io/badge/Output-Markdown_%2B_YAML_%2F_JSON-555.svg)](#output)
[![Skills MCP: unverified](https://img.shields.io/badge/Skills_MCP-unverified-lightgrey.svg)](docs/first-release.md)

**Presentation-style criteria and constraints for ChatGPT and other agents.**

Given existing material, an agent can use Takahashi, Steve Jobs, Wangxing or Bill Gates-inspired analytical guidance to explain how words, focus, visuals and evidence should relate. Each style skill is an independently loadable guide; the route skill helps when the style is undecided.

Designed first for ChatGPT/GPT, the project delivers style guidance and constraints. Consuming tools handle content rewriting, restructuring, slide production and export.

## Choose an entry

| Skill | Identifying relationship | When to use it |
|---|---|---|
| [Takahashi](skills/takahashi-style/SKILL.md) | Words and phrases become primary through relative scale | Key phrases should lead attention |
| [Steve Jobs](skills/jobs-style/SKILL.md) | All elements support one stated focus | Product display, benefits or one comparison |
| [Wangxing](skills/wangxing-style/SKILL.md) | Concise viewpoint and visuals have a meaningful, understandable relationship | Text and visuals should explain a viewpoint together |
| [Bill Gates-inspired analytical style](skills/gates-style/SKILL.md) | Evidence, quantities or system components connect to analysis | Comparisons, test results or system relationships |
| [Style route](skills/presentation-style-route/SKILL.md) | Honor explicit choice; otherwise select one primary style from supplied context | Style is undecided |

Wangxing refers to 張忘形; `wangxing` is a project identifier. These styles are source-led practical syntheses, not creator-endorsed rules, verbatim quotations or official formulas. Dark backgrounds, large type, monochrome, humor and density alone do not establish style identity.

## Get started

1. Obtain the chosen `SKILL.md` and its linked `references/`. A style skill can be used directly.
2. Supply the files through your host's supported attachment, instruction or skill-loading mechanism so it can read references as needed. Typing a skill name does not install it.
3. Provide existing material, purpose and preferences. Use the route if undecided; each request selects one primary style.

After supplying the `jobs-style` definition and references, try:

> Provide Steve Jobs-style guidance and YAML constraints for a battery-life comparison of products A, B, C and D under the same test conditions. Results apply only to this test. I prefer color; retain the comparison conditions.

The skill explains how multiple products can support one comparison while preserving necessary qualifications. Adjustments that undermine the core receive a conflict explanation and a compatible suggestion; unaccepted suggestions are not applied.

## Output

Markdown explains principles, conditions and exceptions, accompanied by default YAML. Explicitly request JSON to switch. Each response uses one structured format; field names and rule identifiers remain English.

```yaml
style_id: jobs
core_rules:
  - rule_id: jobs.single_focus
    constraint: All display and comparison elements support one stated focus; retain conditions needed to understand the comparison.
adjustable_rules: []
```

This is an abbreviated format example; actual constraints depend on the material and full definition. Style does not authorize removing necessary qualifications. No universal fixed word count, font size, pacing or object count is prescribed.

## Verification and limits

Document-contract checks, representative ChatGPT conversation trials and failure/correction records are retained. The [acceptance guide](docs/first-release.md), currently in zh-TW, distinguishes executed trials from reasoned applicability of earlier revisions. These results do not establish reliability across all models, presentation tools or learning outcomes. **Skills MCP dynamic loading compatibility remains unverified.**

Trial records provide relevant inputs, responses and assessments for inspection. Public copies exclude private browser information; the [publication audit](docs/reviews/public-disclosure.md) explains how they differ from original evidence.

## Contribute

Read the [contribution guide](CONTRIBUTING.en.md) and [code of conduct](CODE_OF_CONDUCT.en.md). Changes to sources or style rules should distinguish evidence from project interpretation and include compatible adjustments, conflicts and necessary qualifications.

Development checks (Python 3.11+):

```sh
python3 -m pip install -r requirements-test.txt
python3 -B -m unittest discover -s tests -v
python3 scripts/verify-project.py
python3 scripts/verify-public-content.py
```

Tests check product structure, rule contracts and evidence links; `verify-project.py` checks development collaboration plumbing; `verify-public-content.py` guards known private-information patterns in the working tree, excluding Git history. They do not run ChatGPT or establish Skills MCP loading. Product files live in `skills/`; `.agents/skills/` and `.claude/skills/` contain development tools.

## License

The project and product skills use the [MIT License](LICENSE). Third-party materials retain their original licenses and [notices](THIRD_PARTY_NOTICES.md). Creator and product names identify sources and do not imply affiliation or endorsement.
