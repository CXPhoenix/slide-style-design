# Contributing

[繁體中文（台灣）](CONTRIBUTING.md) · [Project overview](README.en.md)

Contributions to sources, style criteria, examples, translations and verification are welcome. The project provides style constraints; content rewriting, slide production, export tools and automatic mixing are outside its current scope. Follow the [code of conduct](CODE_OF_CONDUCT.en.md).

## Report an issue or propose a change

Search existing issues and PRs first. Reports should include the skill, version or commit, visible host/model/reasoning setting, minimal input, expected result and actual result. Mark unidentified models as unknown. Feature proposals should describe the use case, differences from current criteria and any scope expansion.

**Do not publish private information.** Remove real names, contact details, credentials, private links, browser sidebars and local paths. Use fictional material and share only the relevant response area. Do not post exploitable security details in a public issue; use the repository's private vulnerability reporting feature if enabled, or a private contact method published by the maintainer.

## Make a change and open a PR

1. Create a focused branch in your fork; follow an existing ticket's branch convention when applicable.
2. Product files belong in `skills/`. `.agents/skills/` and `.claude/skills/` serve development collaboration instead.
3. Prefer creator or official public sources. Distinguish direct evidence, sample observations and project synthesis; do not attribute interpretations as verbatim creator rules. Respect source licenses and avoid reproducing entire third-party works.
4. Preserve stable rule identifiers and consistent Markdown/YAML/JSON semantics. Include compatible adjustments, core conflicts and necessary qualifications when rules change.
5. Run the checks below and report results and unverified boundaries. Keep both README, contribution and conduct language versions aligned. Chinese output uses Taiwan Traditional Chinese.
6. Explain the problem, resulting behavior, related issue/ticket, sources, verification and limits. Keep each PR focused on one problem.

```sh
python3 -m pip install -r requirements-test.txt
python3 -B -m unittest discover -s tests -v
python3 scripts/verify-project.py
python3 scripts/verify-public-content.py
```

Python 3.11+ is required. Local tests do not establish ChatGPT behavior; supplied-definition conversation trials do not establish Skills MCP loading. Retain failures and corrections, and do not claim earlier-revision trials were rerun on a new revision. Label sanitized public evidence and its hash boundary; do not describe derived copies as original browser captures.

## Development agents

Read `AGENTS.md` and the linked workflow. Product-rule implementation follows approved specifications, tickets, tests and review gates. Development agents must use the project's `tw-emoji-commit` skill for commits. External contributors do not need to install the full agent toolchain for small documentation corrections; maintainers help determine the applicable workflow.

AI assistance is welcome, but submitters remain responsible for sources, licensing, correctness and privacy. Disclose AI use that materially affects review, especially generated source interpretations or test evidence; private conversations need not be shared.

## Licensing and review

You must have the right to submit your changes. Original contributions are provided under the project's MIT License. Preserve third-party licenses and update `THIRD_PARTY_NOTICES.md` when needed. No additional CLA is currently required. Maintainers may request a smaller scope, better sources or additional verification; merging depends on product scope and evidence.
