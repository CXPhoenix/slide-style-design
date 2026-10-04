# Epic retrospective — 2026-10-04

All T0001–T0014 tickets landed on local main; no remote is configured. The product
contains four independent styles and one route. Approved batch authorization kept
execution moving while preserving per-ticket branches, test tables, independent
reviews and actual ChatGPT surface evidence.

## What to improve next time

1. Audit accepted preferences separately from core compliance. T13 CT04 preserved
   the core but added unrequested decoration reduction; initial manual pass was
   wrong. Independent T14 review caught it, old verdict retained as history, active
   failed record plus a new candidate/affected run now support acceptance. Compare
   every optional constraint against actual caller acceptance, not generic examples.
2. Freeze every changed layer before review. The initial T14 helper omitted complete
   new README/guide and historical context files and used a stale pending exclusion.
   Supplemental scope/hashes restored independent full-scope review; future packet
   preparation should derive the changed-file inventory and verify all paths present.
3. Keep UI operations bounded and inspect after timeouts before sending again.
   CT05 draft was confirmed unsent before submission; original conversations/raw
   responses were recovered where possible. Do not treat transport/capture faults as
   model verdicts, or repeated sampling as a correction.
4. Preserve acceptance distinctions: file/schema checks, actual supplied-definition
   ChatGPT results, revision-applicability inference and dynamic MCP loading are
   separate claims. Exact underlying default model was not displayed; use visible
   Medium and host limits, not a guessed model name.

No new approval gate or source-backed numerical rule is introduced. Existing spec
and test retry rules remain authoritative. Stable evidence-correction practice is
recorded in ADR0004; unresolved next-epic decisions in OPEN-QUESTIONS.md.
