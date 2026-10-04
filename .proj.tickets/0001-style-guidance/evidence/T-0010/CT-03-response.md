## Wangxing Style Guidance

The selected style is **Wangxing (張忘形)**. `wangxing` is the project identifier, not an official English name. The analytical nature of the material does **not** change the explicitly selected style. 貼上的文字 (1)

The mandatory rule is `wangxing.text_visual_relation`: concise viewpoint text and the visual representation must communicate the same viewpoint or an explicitly named relationship, and the visual must materially contribute to understanding rather than function as decoration. 貼上的文字 (1)

For this case, the task blocks should visibly correspond to each person's responsibility. That mapping supports the viewpoint about responsibilities **within this team only**; the qualification must not be generalized beyond the supplied context. Because the material is intended for independent reading, the viewpoint, task/person relationship, and necessary qualifications must remain understandable without a speaker supplying missing context. 貼上的文字 (1)

Using **color** and **no humor** is compatible with the Wangxing core and is accepted here as `wangxing.presentation_preferences`. Neither changes the requirement for a meaningful viewpoint-to-visual relationship. 貼上的文字 (1)

```json
{
  "style_id": "wangxing",
  "core_rules": [
    {
      "rule_id": "wangxing.text_visual_relation",
      "constraint": "Concise viewpoint text and visuals must communicate the same viewpoint or an explicitly named relationship, and the visual must contribute to understanding rather than serve as decoration. Task blocks map clearly to each person's responsibility, supporting the responsibility relationship within this team only. For independent reading, the viewpoint, task/person correspondence, and all necessary qualifications must remain understandable without speaker supplementation."
    }
  ],
  "adjustable_rules": [
    {
      "rule_id": "wangxing.presentation_preferences",
      "constraint": "Use color and no humor while retaining the meaningful correspondence between task blocks and each person's responsibility. Preserve the limitation to this team, and ensure all information needed for independent reading remains understandable without a speaker."
    }
  ]
}
```