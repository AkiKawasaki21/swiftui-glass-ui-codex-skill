# Security Policy

This repository contains a Codex Skill and supporting documentation. It should not request secrets, credentials, payment details, or private user data.

If you use this skill inside an app repository, review Codex changes before merging.

The skill explicitly instructs Codex not to modify authentication, authorization, payments, subscriptions, networking, persistence, analytics, permissions, routing behavior, or business logic.

Report a security concern if the skill:

- asks for secrets or credentials
- encourages editing payment, authentication, persistence, networking, analytics, or permission code
- weakens accessibility or privacy-related UI signals
- makes non-UI changes while performing a visual redesign

Report concerns by opening an issue with a clear description and reproduction steps.
