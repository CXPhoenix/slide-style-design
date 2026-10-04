# T-0001 red/green record

## Cycle 1 — direct entry

Red: entry test fails because Jobs SKILL.md is absent (red-01.log).
Minimal entry: named metadata, concise description, scope sentence.
Green: one entry check passes (green-01.log). This does not establish core semantics.

## Cycle 2 — core/source record

Manual red observed before core implementation: the entry is only metadata and a
scope sentence. It lacks jobs.single_focus, the stated-focal-point relationship,
supporting text/visual relationship, source classification/reading limits and
compatible/conflicting examples required by the accepted spec. These mandatory
propositions, not the entry's wording, are the semantic oracle.

Manual green: entry/core record contain both required relationships, source-led
classification, limits and examples, including several objects serving one point.
Conditions remain explicit and numerical/global-narrative mandates are disclaimed.
Independent review follows; this is not an actual ChatGPT result.

## Cycle 3 — YAML handoff

Red: newly added handoff check fails because the example is absent; entry remains
green (red-03.log). Minimal implementation adds the example and on-demand pointer.
Green: both Jobs checks pass (green-03.log). Schema/type/ID parsing is distinct from
semantic document review. Existing Takahashi checks are unchanged.
