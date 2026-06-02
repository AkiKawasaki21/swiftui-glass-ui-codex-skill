# Release Workflow

Use this checklist when publishing a new version of the SwiftUI Glass UI Designer skill.

## Before Tagging

1. Review the skill scope.
   - Confirm `SKILL.md` still targets SwiftUI macOS visual-system work.
   - Confirm negative scope still excludes business logic, models, networking, persistence, auth, payments, subscriptions, analytics, signing, and deployment-target changes.
2. Update examples and evals.
   - Add positive eval prompts for any new trigger behavior.
   - Add negative eval prompts for any likely false-positive area.
   - Keep `examples/invocation.md` and `.agents/skills/swiftui-glass-ui-designer/references/EXAMPLE_PROMPTS.md` aligned.
3. Update release metadata.
   - Set `VERSION` to the release version, such as `0.2.0`.
   - Add a matching `## 0.2.0 - Summary` entry to `CHANGELOG.md`.
4. Validate locally.

```bash
python3 scripts/validate_repo.py
```

## GitHub Release

1. Commit the release changes.
2. Push to GitHub and confirm the `Validate Skill Repo` workflow passes.
3. Tag the version from the release commit.

```bash
git tag v0.2.0
git push origin v0.2.0
```

4. Create a GitHub release from the tag.
   - Use the matching `CHANGELOG.md` entry as the release notes.
   - Mention that this is a Codex Skill instruction bundle, not a Swift package.
   - Include install commands for global and per-app installation.

## After Release

- Install the released skill in a clean target app or global skills folder.
- Run one audit-only invocation and one conservative polish invocation from `examples/invocation.md`.
- If either prompt reveals drift, update the skill docs and evals before the next release.
