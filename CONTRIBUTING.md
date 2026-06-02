# Contributing

Contributions are welcome.

Good contributions include:

- clearer skill instructions
- better trigger descriptions
- safer negative-scope rules
- improved accessibility guidance
- better SwiftUI component patterns
- real-world notes from macOS apps, without private app details
- eval prompts that catch false positives or weak implementations

Please avoid contributions that:

- encourage changing business logic
- make the skill depend on one private app structure
- overfit the skill to a single visual style
- remove accessibility fallbacks
- add unnecessary scripts when instructions are enough

## Development checklist

Before opening a PR:

- [ ] `SKILL.md` still has clear `name` and `description` front matter.
- [ ] Trigger scope is clear.
- [ ] Negative scope is clear.
- [ ] The UI-only safety contract remains explicit.
- [ ] Instructions remain action-oriented.
- [ ] Accessibility guidance remains present.
- [ ] Example prompts still work with the skill name.
- [ ] `evals/skill-prompts.csv` covers new trigger behavior.
- [ ] `python3 scripts/validate_repo.py` passes.
- [ ] `VERSION`, `CHANGELOG.md`, and `RELEASE.md` are updated for release-oriented changes.

Keep the repo focused. Prefer updating `SKILL.md` or an existing reference file before adding new files.
