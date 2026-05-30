# SwiftUI Glass UI Designer Skill

A focused Codex Skill for upgrading existing SwiftUI macOS apps with a polished, native, glass-style interface.

The skill helps Codex inspect an app, create or extend a small reusable design system, apply translucent panels/cards/buttons/navigation consistently, support accessibility fallbacks, build the project, and report exactly what changed. It is opinionated about restraint: the goal is a native macOS glass UI, not blur applied everywhere.

## What This Is

This repository publishes one Codex Skill:

```text
.agents/skills/swiftui-glass-ui-designer/SKILL.md
```

It is an instruction bundle, not a Swift package or drop-in UI library. Codex adapts the guidance to the target app's structure.

## Who This Is For

Use this if you are a developer with an existing SwiftUI macOS app and you want Codex to perform a focused visual-system pass: app shell, navigation, cards, panels, buttons, settings, onboarding, menu-bar popovers, light/dark mode, and Reduce Transparency support.

This is not for new product features, backend work, generic web glassmorphism, or non-SwiftUI apps.

## What Codex Should Change

Codex should limit changes to presentation-layer SwiftUI code:

- SwiftUI views, modifiers, button styles, navigation styles, sheets, cards, panels, and visual tokens
- small reusable design-system files such as `GlassTheme.swift`, `GlassPanel.swift`, `GlassButton.swift`, or `GlassModifiers.swift`
- preview-only or visual asset tweaks when they do not affect runtime behavior

Codex should not change:

- business logic, feature behavior, user flows, routing behavior, or navigation destinations
- models, stores, reducers, controllers, services, clients, repositories, dependency containers, or calculations
- networking, persistence, authentication, authorization, payments, subscriptions, analytics, telemetry, permissions, entitlements, signing, dependencies, bundle identifiers, or deployment targets

## Installation

Choose one installation style.

### Copy Into One App

Use this when one SwiftUI macOS app repository should carry the skill with it:

```bash
SKILL_REPO="/path/to/swiftui-glass-ui-codex-skill"
TARGET_REPO="/path/to/your/swiftui-macos-app"

mkdir -p "$TARGET_REPO/.agents/skills"
cp -R "$SKILL_REPO/.agents/skills/swiftui-glass-ui-designer" "$TARGET_REPO/.agents/skills/"
test -f "$TARGET_REPO/.agents/skills/swiftui-glass-ui-designer/SKILL.md"
```

After copying, open the target app repository in Codex and invoke the skill from that repo root.

### Global install

Use this when you want the skill available across repositories in your Codex setup:

```bash
SKILL_REPO="/path/to/swiftui-glass-ui-codex-skill"
SKILL_HOME="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$SKILL_HOME"
cp -R "$SKILL_REPO/.agents/skills/swiftui-glass-ui-designer" "$SKILL_HOME/"
test -f "$SKILL_HOME/swiftui-glass-ui-designer/SKILL.md"
```

Restart Codex if the skill is not discovered immediately.

## Invocation

Invoke the skill explicitly from inside an existing SwiftUI macOS app repository:

```text
Use $swiftui-glass-ui-designer to upgrade this SwiftUI macOS app with a premium native glass-style interface. Inspect the project first, create a reusable design system, apply it consistently, preserve all business logic, build the app, and summarize changed files.
```

More examples are in [examples/invocation.md](examples/invocation.md).

## Expected Result

A good run should produce a small, reusable SwiftUI visual system and apply it to the main app surfaces. It should not rewrite the product. Expect Codex to favor a few strong decisions: one calm background treatment, consistent material strengths, shared corner radii, readable strokes, subtle shadows, capsule selected states, and solid fallbacks when Reduce Transparency is enabled.

## Included Files

```text
.agents/skills/swiftui-glass-ui-designer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── ACCESSIBILITY_RULES.md
│   ├── DESIGN_PRINCIPLES.md
│   ├── EXAMPLE_PROMPTS.md
│   ├── IMPLEMENTATION_CHECKLIST.md
│   ├── REVIEW_RUBRIC.md
│   └── SWIFTUI_COMPONENT_PATTERNS.md
└── scripts/
    └── find_swiftui_views.py
```

The helper script is optional and read-only:

```bash
python3 .agents/skills/swiftui-glass-ui-designer/scripts/find_swiftui_views.py
```

Run it from a target app repository to list likely SwiftUI view files before a redesign pass.

## Developer Workflow

Keep the repository small. Put core operating instructions in `SKILL.md`, detailed guidance in `references/`, and deterministic helpers in `scripts/`.

Before publishing or opening a PR, run the dependency-free validator:

```bash
python3 scripts/validate_repo.py
```

The validator checks required files, skill metadata, README safety/install coverage, helper-script syntax, eval CSV shape, example references, and generated-artifact hygiene.

Also review [evals/skill-prompts.csv](evals/skill-prompts.csv) when changing trigger scope. It should include positive prompts for SwiftUI macOS glass redesigns and negative prompts for backend, payments, auth, database, web, and unrelated Swift work.

## Quality Expectations

A successful skill run should:

- inspect before editing
- create reusable SwiftUI presentation components or modifiers
- avoid changing business logic
- preserve existing app behavior and navigation
- improve visual consistency
- support light mode, dark mode, and Reduce Transparency
- build the app or report the exact environmental blocker
- list changed files and verification steps

## License

MIT License. See [LICENSE](LICENSE).
