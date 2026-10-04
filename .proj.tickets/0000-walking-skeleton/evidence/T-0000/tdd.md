# T-0000 red/green record

The approved plan is [test-plan.md](test-plan.md). These are document/structure
checks, not actual ChatGPT results.

## Cycle 1 — TP-01 direct entry

- Red: the entry test fails with FileNotFoundError because the published Takahashi
  entry does not exist. One test was written before the entry.
- Minimal implementation: add a named direct-use skill entry and concise description.
- Green: the single entry test passes. Semantic core/source requirements are still
  missing and are not inferred from metadata passing.

## Cycle 2 — TP-02 semantic core/source record

Manual red observation before implementation: the current entry contains only a
scope sentence. It does not declare `takahashi.text_primary`, relative-scale
priority, the conditional subordinate role of other detail, or a source record with
classification, conditions, evidence limits, and boundary examples. This fails the
accepted core record; the oracle is the spec, not the entry's own wording.

Manual green: the entry now states all three propositions, and its accessible
core/source record classifies the rule as core/project synthesis, explains T1/T2
and their reading limits, preserves the conditional supporting-detail relationship,
and supplies the accepted compatible/conflicting examples. It avoids a numerical
threshold and a universal chart ban. The existing structural entry/link test also
passes. Independent review is recorded separately; this is not a ChatGPT result.

## Cycle 3 — TP-03 published YAML handoff

- Red: add the single published-handoff contract test; it fails because the handoff
  example is absent. The already-green entry test remains green.
- Minimal implementation: add an illustrative Markdown/YAML handoff and an on-demand
  pointer. The fixed core ID and all three required propositions occur in both
  representations, including the conditional supporting-detail relationship.
- Green: both product tests pass (see [green-03.log](green-03.log)).
  Parsing/type/ID checks cover structure; document review covers meaning. Neither
  is a ChatGPT observation.
