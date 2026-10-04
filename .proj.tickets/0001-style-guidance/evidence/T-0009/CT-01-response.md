## Wangxing style guidance

This style refers to Zhang Wangxing (張忘形); `wangxing` is the project identifier, not a claim about an official English name. The mandatory core rule is `wangxing.text_visual_relation`: concise viewpoint text and a visual representation must communicate the same viewpoint or an explicitly identifiable relationship, and the visual must contribute to understanding rather than function as decoration. 貼上的文字 (1)

For these independently read social graphics, keep the claim specifically limited to **this team**: clear task division helps reduce duplicate work. The existing visual should make that relationship inspectable by mapping task blocks to each person's responsibilities. Preserve the team-specific qualification rather than generalizing the statement beyond the supplied context. 貼上的文字 (1)

Because no speaker is present, the viewpoint, the task-to-person visual mapping, and every qualification needed to interpret the claim must remain understandable from the graphic itself. Do not rely on omitted context being supplied orally. 貼上的文字 (1)

Color and the absence of humor are accepted compatible preferences. Neither changes the required meaningful relationship between the concise viewpoint and the responsibility mapping; monochrome treatment and memes are not mandatory characteristics of the style. 貼上的文字 (1)

These are expression constraints only. They do not authorize rewriting, restructuring, reorganizing, replacing illustrations, or otherwise transforming the supplied material. 貼上的文字 (1)

```yaml
style_id: wangxing
core_rules:
  - rule_id: wangxing.text_visual_relation
    constraint: >-
      Concise viewpoint text and the visual representation must communicate the same
      viewpoint or an explicitly identifiable relationship, and the visual must
      contribute to understanding rather than serve as decoration. For this team,
      the viewpoint is that clear task division helps reduce duplicate work, and the
      visual maps task blocks to each person's responsibilities so that relationship
      is understandable. Keep the statement limited to this team. Because the graphic
      is independently read, the viewpoint, visual relationship, and all necessary
      qualifications must remain understandable without a speaker supplying missing
      information.
adjustable_rules:
  - rule_id: wangxing.presentation_preferences
    constraint: >-
      Use color and no humor while preserving the meaningful relationship between the
      concise viewpoint and the task-block-to-person responsibility mapping. Keep the
      team-specific qualification visible and understandable, and do not rely on a
      speaker to supply omitted meaning or conditions.
```