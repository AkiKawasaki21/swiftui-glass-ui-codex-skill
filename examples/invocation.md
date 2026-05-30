# Invocation Examples

Use these prompts from the root of a SwiftUI macOS app after installing the skill. Prefer explicit invocation with `$swiftui-glass-ui-designer` when you want predictable behavior.

## Full app redesign

```text
Use $swiftui-glass-ui-designer to upgrade this SwiftUI macOS app with a premium native glass-style interface. Inspect the project first, create a reusable design system, apply it consistently, preserve all business logic, build the app, and summarize changed files.
```

## Conservative first pass

```text
Use $swiftui-glass-ui-designer for a conservative first pass. Inspect the project, identify UI files and off-limits logic files, create reusable glass components, polish the app shell, cards, navigation, and buttons, preserve all behavior, then build the app.
```

## Existing UI cleanup

```text
Use $swiftui-glass-ui-designer to clean up the current glass UI. Keep the existing layout mostly intact, reduce duplicated visual styling, improve readability, ensure light mode, dark mode, and Reduce Transparency all work, and do not edit business logic.
```

## Menu bar app polish

```text
Use $swiftui-glass-ui-designer to polish this SwiftUI macOS menu-bar app interface. Focus on the popover, settings screen, onboarding, cards, buttons, hover states, focus states, and visual consistency. Preserve all feature behavior and do not edit services, stores, networking, persistence, authentication, payments, or analytics.
```

## Accessibility pass

```text
Use $swiftui-glass-ui-designer to audit and fix the glass UI for accessibility. Check Reduce Transparency, light mode, dark mode, contrast, keyboard focus, hover states, selected states, and duplicated visual styling. Fix UI issues only and preserve behavior.
```

## Design-system extraction

```text
Use $swiftui-glass-ui-designer to refactor scattered glass styling into reusable SwiftUI components, modifiers, styles, and tokens. Preserve the current look and behavior as much as possible, avoid business logic files, and build the app afterward.
```

## Audit only

```text
Use $swiftui-glass-ui-designer to audit the current UI implementation. Do not edit yet. Identify likely UI files, files that should remain off-limits, duplicated glass styling, weak contrast, screens needing polish, accessibility gaps, and design-system files that should be created.
```
