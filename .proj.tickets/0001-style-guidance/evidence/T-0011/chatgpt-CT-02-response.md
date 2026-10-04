For comparing **measured energy use**, the selected style is **Bill Gates-inspired analytical style (`gates`)**. The routing guidance explicitly maps interpretation or comparison of measured quantities to the Gates analytical focus, and its example specifically identifies measured energy comparison as an eligible Gates case. 貼上的文字 (1) 貼上的文字 (1)

### Bill Gates-inspired style guidance

Apply `gates.evidence_relation` as the mandatory core rule:

- Relate the measured energy evidence or quantities to a **clearly stated comparison point**. The numbers should communicate what is being compared rather than appear as isolated values.
- Preserve any **labels, units, assumptions, measurement conditions, or qualifications** that are necessary to interpret the supplied measurements correctly.
- Use hierarchy, spacing, and relevant annotations to make the relationship between evidence and comparison clear.
- High information density is **not** required. More whitespace or fewer decorative elements are compatible as long as the evidence relationship and interpretation-critical information remain intact.
- Do not invent missing assumptions merely to fill a presentation template. 貼上的文字 (1) 貼上的文字 (1)

This is a source-led project synthesis inspired by Gates's analytical orientation, not an official or universal “Bill Gates presentation method.” This guidance does not calculate the measurements, rewrite the argument, restructure slides, or produce the presentation. 貼上的文字 (1) 貼上的文字 (1)

```yaml
style_id: gates
core_rules:
  - rule_id: gates.evidence_relation
    constraint: >-
      Relate the supplied measured-energy evidence, quantities, or relevant system
      elements to a clearly stated comparison or system point. Preserve labels,
      units, assumptions, measurement conditions, and qualifications whenever they
      are necessary to interpret the supplied evidence correctly. Use hierarchy,
      spacing, and relevant annotations to make the analytical relationship clear;
      whitespace or reduced decoration may be used without removing interpretation-
      critical information, and high density is not required. Do not invent missing
      assumptions or convert measurements into disconnected decorative quantities.
adjustable_rules: []
```