# T-0003 red/green record

## Cycle 1 — direct entry

Red: named-entry check fails because Gates SKILL.md is absent (red-01.log).
Minimal entry: name/description and scope sentence.
Green: one entry check passes (green-01.log), not a semantic/core pass.

## Cycle 2 — core/source

Manual red before core implementation: entry lacks gates.evidence_relation,
evidence/quantity/system-to-stated-point relationships, conditional interpretation
labels/units/assumptions/qualifiers, source classification/limits and boundary cases.
Accepted spec propositions are the independent oracle, not the entry's wording.

Manual green: entry/source record preserves required relationships and conditional
qualifiers, classification, reading limits and compatible/conflicting examples.
No official method/density formula claimed. Independent review follows; not a ChatGPT result.

## Cycle 3 — handoff

Red: handoff check fails because example is absent; entry stays green (red-03.log).
Minimal implementation: complementary example and on-demand pointer.
Green: both Gates structural checks pass (green-03.log). Meaning/conditions reviewed
separately; schema parsing does not establish actual model behavior.

## Cycle 4 — actual ChatGPT scope failure

Red: candidate 01 CT-01 recommends appendix relocation in Markdown and detail splitting in YAML, violating AC-02; complete failed response and input retained in candidates/candidate-01/. CT-02 passes but cannot waive this failure.

Minimal correction: entry boundary now explicitly covers recommendations in both representations and excludes splitting/appendix relocation; projection advice stays within hierarchy, spacing and annotations. Local document inspection verifies the clarification, not actual ChatGPT behavior. Candidate 02 must rerun both unchanged requests.

Cycle 4 actual green: candidate 02 full user-supplied CT-01/02 replies pass every approved check; no split/appendix recommendation. Both default model/medium; exact model unknown. Results and hashes recorded, prior red retained.
