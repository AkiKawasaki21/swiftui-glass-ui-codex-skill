#!/usr/bin/env python3
"""Validate the SwiftUI Glass UI Designer skill repository."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "swiftui-glass-ui-designer"
SKILL_DIR = ROOT / ".agents" / "skills" / SKILL_NAME
SKILL_MD = SKILL_DIR / "SKILL.md"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "CHANGELOG.md",
    ROOT / "RELEASE.md",
    ROOT / "VERSION",
    ROOT / ".gitignore",
    ROOT / ".github" / "pull_request_template.md",
    ROOT / ".github" / "workflows" / "validate.yml",
    ROOT / "examples" / "invocation.md",
    ROOT / "evals" / "skill-prompts.csv",
    SKILL_MD,
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "scripts" / "find_swiftui_views.py",
]

REQUIRED_REFERENCES = [
    "ACCESSIBILITY_RULES.md",
    "DESIGN_PRINCIPLES.md",
    "EXAMPLE_PROMPTS.md",
    "IMPLEMENTATION_CHECKLIST.md",
    "REVIEW_RUBRIC.md",
    "SWIFTUI_COMPONENT_PATTERNS.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append("SKILL.md must start with YAML frontmatter.")
        return {}

    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append("SKILL.md frontmatter must end with '---'.")
        return {}

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    for name in REQUIRED_REFERENCES:
        path = SKILL_DIR / "references" / name
        if not path.is_file():
            errors.append(f"Missing required reference: {path.relative_to(ROOT)}")


def check_skill_md(errors: list[str]) -> None:
    if not SKILL_MD.is_file():
        return

    text = read_text(SKILL_MD)
    frontmatter = parse_frontmatter(text, errors)

    if set(frontmatter) != {"name", "description"}:
        errors.append("SKILL.md frontmatter should contain only 'name' and 'description'.")
    if frontmatter.get("name") != SKILL_NAME:
        errors.append(f"SKILL.md name must be {SKILL_NAME!r}.")
    if not re.fullmatch(r"[a-z0-9-]+", frontmatter.get("name", "")):
        errors.append("SKILL.md name must use lowercase letters, digits, and hyphens only.")

    description = frontmatter.get("description", "")
    for term in ("SwiftUI", "macOS", "business logic", "models", "networking", "persistence", "subscriptions", "Do not use"):
        if term not in description:
            errors.append(f"SKILL.md description should mention {term!r}.")

    body = text.lower()
    for phrase in (
        "never change business logic",
        "do not add `.blur`",
        "references/implementation_checklist.md",
        "references/accessibility_rules.md",
        "scripts/find_swiftui_views.py",
        "git diff",
    ):
        if phrase not in body:
            errors.append(f"SKILL.md should include {phrase!r}.")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md should stay under 500 lines.")


def check_openai_yaml(errors: list[str]) -> None:
    path = SKILL_DIR / "agents" / "openai.yaml"
    if not path.is_file():
        return

    text = read_text(path)
    for phrase in ("display_name:", "short_description:", "default_prompt:", SKILL_NAME):
        if phrase not in text:
            errors.append(f"openai.yaml should include {phrase!r}.")


def check_readme(errors: list[str]) -> None:
    path = ROOT / "README.md"
    if not path.is_file():
        return

    text = read_text(path)
    for phrase in (
        "Who This Is For",
        "What Codex Should Change",
        "Copy Into One App",
        "$TARGET_REPO/.agents/skills",
        "$swiftui-glass-ui-designer",
        "business logic",
        "models",
        "networking",
        "persistence",
        "authentication",
        "payments",
        "subscriptions",
        "RELEASE.md",
        "python3 scripts/validate_repo.py",
    ):
        if phrase not in text:
            errors.append(f"README.md should include {phrase!r}.")


def check_release_metadata(errors: list[str]) -> None:
    version_path = ROOT / "VERSION"
    changelog_path = ROOT / "CHANGELOG.md"
    release_path = ROOT / "RELEASE.md"

    if not version_path.is_file():
        return

    version = read_text(version_path).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must use semantic version format like 0.1.0.")

    if changelog_path.is_file():
        changelog = read_text(changelog_path)
        if f"## {version}" not in changelog:
            errors.append(f"CHANGELOG.md must include an entry for VERSION {version}.")

    if release_path.is_file():
        release = read_text(release_path)
        for phrase in (
            "python3 scripts/validate_repo.py",
            "git tag v",
            "GitHub release",
            "CHANGELOG.md",
            "Codex Skill instruction bundle",
        ):
            if phrase not in release:
                errors.append(f"RELEASE.md should include {phrase!r}.")


def check_github_workflow(errors: list[str]) -> None:
    workflow_path = ROOT / ".github" / "workflows" / "validate.yml"
    if not workflow_path.is_file():
        return

    text = read_text(workflow_path)
    for phrase in (
        "permissions:",
        "contents: read",
        "concurrency:",
        "timeout-minutes:",
        "python3 -m py_compile scripts/validate_repo.py",
        "python3 scripts/validate_repo.py",
    ):
        if phrase not in text:
            errors.append(f".github/workflows/validate.yml should include {phrase!r}.")


def check_pull_request_template(errors: list[str]) -> None:
    path = ROOT / ".github" / "pull_request_template.md"
    if not path.is_file():
        return

    text = read_text(path)
    for phrase in (
        "Skill Scope",
        "UI-only safety contract",
        "business logic",
        "python3 scripts/validate_repo.py",
        "evals/skill-prompts.csv",
    ):
        if phrase not in text:
            errors.append(f".github/pull_request_template.md should include {phrase!r}.")


def check_eval_csv(errors: list[str]) -> None:
    path = ROOT / "evals" / "skill-prompts.csv"
    if not path.is_file():
        return

    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    if not rows:
        errors.append("evals/skill-prompts.csv must contain at least one prompt.")
        return

    expected_headers = {"id", "should_trigger", "prompt"}
    if set(rows[0]) != expected_headers:
        errors.append("evals/skill-prompts.csv headers must be id,should_trigger,prompt.")

    seen_ids: set[str] = set()
    trigger_values: set[str] = set()
    positive_count = 0
    negative_count = 0
    for row in rows:
        row_id = row.get("id", "")
        if not row_id:
            errors.append("Eval row is missing an id.")
        if row_id in seen_ids:
            errors.append(f"Duplicate eval id: {row_id}")
        seen_ids.add(row_id)

        should_trigger = row.get("should_trigger", "")
        if should_trigger not in {"true", "false"}:
            errors.append(f"Eval {row_id} has invalid should_trigger value: {should_trigger!r}")
        trigger_values.add(should_trigger)
        if should_trigger == "true":
            positive_count += 1
        if should_trigger == "false":
            negative_count += 1

        if not row.get("prompt"):
            errors.append(f"Eval {row_id} is missing a prompt.")

    if trigger_values != {"true", "false"}:
        errors.append("Eval CSV must include both triggering and non-triggering prompts.")
    if positive_count < 5:
        errors.append("Eval CSV should include at least five triggering prompts.")
    if negative_count < 8:
        errors.append("Eval CSV should include at least eight non-triggering prompts.")


def check_examples(errors: list[str]) -> None:
    paths = [
        ROOT / "README.md",
        ROOT / "examples" / "invocation.md",
        SKILL_DIR / "references" / "EXAMPLE_PROMPTS.md",
    ]
    for path in paths:
        if not path.is_file():
            continue
        text = read_text(path)
        if f"${SKILL_NAME}" not in text:
            errors.append(f"{path.relative_to(ROOT)} should include an explicit skill invocation.")
        if "business logic" not in text:
            errors.append(f"{path.relative_to(ROOT)} should mention preserving business logic.")

    invocation = ROOT / "examples" / "invocation.md"
    reference_examples = SKILL_DIR / "references" / "EXAMPLE_PROMPTS.md"
    if invocation.is_file() and "Release smoke test" not in read_text(invocation):
        errors.append("examples/invocation.md should include a release smoke test prompt.")
    if reference_examples.is_file() and "Release smoke test" not in read_text(reference_examples):
        errors.append("references/EXAMPLE_PROMPTS.md should include a release smoke test prompt.")


def check_helper_script(errors: list[str]) -> None:
    path = SKILL_DIR / "scripts" / "find_swiftui_views.py"
    if not path.is_file():
        return

    try:
        compile(read_text(path), str(path), "exec")
    except SyntaxError as exc:
        errors.append(f"Helper script syntax error: {exc}")


def check_generated_artifacts(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if "__pycache__" in path.parts:
            errors.append(f"Generated cache directory should not be committed: {path.relative_to(ROOT)}")
        if path.suffix in {".pyc", ".pyo"}:
            errors.append(f"Generated Python bytecode should not be committed: {path.relative_to(ROOT)}")


def check_gitignore(errors: list[str]) -> None:
    path = ROOT / ".gitignore"
    if not path.is_file():
        return

    text = read_text(path)
    for phrase in (".DS_Store", "__pycache__/", "*.py[cod]", ".pytest_cache/", ".build/", "DerivedData/"):
        if phrase not in text:
            errors.append(f".gitignore should include {phrase!r}.")


def main() -> int:
    errors: list[str] = []

    check_required_files(errors)
    check_skill_md(errors)
    check_openai_yaml(errors)
    check_readme(errors)
    check_release_metadata(errors)
    check_github_workflow(errors)
    check_pull_request_template(errors)
    check_eval_csv(errors)
    check_examples(errors)
    check_helper_script(errors)
    check_generated_artifacts(errors)
    check_gitignore(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
