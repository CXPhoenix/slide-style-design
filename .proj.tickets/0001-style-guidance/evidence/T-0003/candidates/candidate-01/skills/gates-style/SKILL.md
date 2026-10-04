---
name: gates-style
description: Provide Bill Gates-inspired analytical presentation-style guidance when requested, relating evidence, quantities or system elements to a stated analytical point.
---

# Bill Gates-inspired style

Provide reusable style guidance directly. Content transformation and presentation
production belong to consuming tools.

## Identifying core

`gates.evidence_relation` is the mandatory core rule:

- Analytical guidance relates evidence, quantities or system elements to a stated
  comparison or system point. Explain what the evidence supports, what is being
  compared, or how the system elements relate; isolated numbers are not enough.
- When labels, units, assumptions or qualifications are necessary to interpret
  supplied evidence, retain those relationships and qualifiers. Density or brevity
  cannot justify removing them.

Use hierarchy and relevant annotations to make the analytical relationship readable.
Whitespace or fewer decorative elements can retain this core. High density, all
arguments on one page, or charts without a stated relationship are not requirements.

This is source-led project synthesis inspired by Bill Gates's analytical orientation,
not a quotation or official creator method. Consult the [core/source record](references/core-rule.md)
for evidence, applicability, reading limits or boundary examples. The core above
is sufficient for direct use; no route prerequisite applies.

## Guidance boundary

Use supplied material as context for style constraints. Preserve necessary metric
labels, units, comparison assumptions, system labels and applicability limits.
Do not turn test-specific results into general claims or interpret a quantity as
unqualified decoration. Conditions apply when needed for interpretation, not as a
requirement to invent missing assumptions or labels.

Return style guidance rather than calculated results, rewritten arguments, invented
evidence, page plans, whole-deck narratives or presentation files. Consuming tools
may separately perform authorized analysis/content/production work. This skill
explains expression relationships rather than executing those operations.
Do not attribute fixed timing, word counts, density thresholds or an obligatory
no-story/no-humor rule to the creator without supporting evidence.

## Core/YAML handoff

This increment returns Taiwan Traditional Chinese guidance with English fields
and rule IDs. Other language variants, JSON switching, adjustment handling and
route behavior are separate increments.

Return complementary Markdown and exactly one YAML settings block. Identify Bill
Gates-inspired style and `gates.evidence_relation` in the explanation. Markdown
and constraint both retain the stated evidence/comparison/system relationship and
all interpretation-critical labels, units, assumptions and qualifications when
applicable. Source reasoning and illustrative examples may stay Markdown-only.

Use `style_id: gates`, `core_rules` with the mandatory record, and
`adjustable_rules: []`. Records have unique nonempty English `rule_id` values and
nonempty string `constraint` values; YAML uses JSON-compatible types without
custom tags. Finish when guidance/settings agree on meaning and applicable
conditions. Consult the [handoff example](references/handoff-example.md) for output
shape; wording may vary without changing identity or meaning.

If requested supporting material is inaccessible, disclose that limit rather than
invent contents. No shell, local filesystem or connected MCP service is assumed.
