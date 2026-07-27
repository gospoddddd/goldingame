#!/usr/bin/env python3
"""Validate Redraft's project configuration and durable knowledge structure."""

from __future__ import annotations

import json
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault"
TEMPLATES = VAULT / "90 Templates"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FRONTMATTER_ID = re.compile(r"^id:\s*(.+?)\s*$", re.MULTILINE)
SKILL_NAME = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
SKILL_DESCRIPTION = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)
REQUIRED_FILES = [
    "AGENTS.md",
    "CONTRIBUTING.md",
    "Makefile",
    "README.md",
    ".codex/config.toml",
    ".codex/hooks.json",
    ".codex/hooks/stop_validate_workspace.py",
    ".codex/rules/external-actions.rules",
    ".github/pull_request_template.md",
    ".github/workflows/workspace-quality.yml",
    "vault/00 Home/Project Home.md",
    "vault/00 Home/Current Context.md",
    "vault/50 Decisions/ADR-0002 Repository governance.md",
    "vault/70 Operations/Risk Register.md",
]


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def collect_files() -> tuple[list[Path], list[Path], list[Path]]:
    markdown = sorted(VAULT.rglob("*.md"))
    toml = [ROOT / ".codex" / "config.toml"]
    toml.extend(sorted((ROOT / ".codex" / "agents").glob("*.toml")))
    json_files = [ROOT / ".codex" / "hooks.json"]
    json_files.extend(sorted((VAULT / ".obsidian").glob("*.json")))
    return markdown, toml, json_files


def validate_required_structure(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"{relative_path}: required project file is missing")

    workflow = ROOT / ".github" / "workflows" / "workspace-quality.yml"
    if workflow.is_file():
        text = workflow.read_text(encoding="utf-8")
        for required_fragment in [
            "permissions:",
            "contents: read",
            "make check",
        ]:
            if required_fragment not in text:
                errors.append(
                    f"{relative(workflow)}: missing {required_fragment!r}"
                )


def validate_serialized(
    toml_files: list[Path], json_files: list[Path], errors: list[str]
) -> None:
    for path in toml_files:
        try:
            with path.open("rb") as handle:
                tomllib.load(handle)
        except Exception as exc:  # noqa: BLE001 - report every parse failure together
            errors.append(f"{relative(path)}: invalid TOML: {exc}")

    for path in json_files:
        try:
            with path.open(encoding="utf-8") as handle:
                json.load(handle)
        except Exception as exc:  # noqa: BLE001 - report every parse failure together
            errors.append(f"{relative(path)}: invalid JSON: {exc}")


def validate_skills(errors: list[str]) -> int:
    skill_files = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        name = SKILL_NAME.search(text)
        description = SKILL_DESCRIPTION.search(text)
        if not name:
            errors.append(f"{relative(path)}: missing valid skill name")
        elif name.group(1) != path.parent.name:
            errors.append(
                f"{relative(path)}: name {name.group(1)!r} does not match directory"
            )
        if not description or "TODO" in description.group(1):
            errors.append(f"{relative(path)}: missing completed description")
        if "TODO" in text or "FIXME" in text:
            errors.append(f"{relative(path)}: contains TODO or FIXME")
        if not (path.parent / "agents" / "openai.yaml").is_file():
            errors.append(f"{relative(path.parent)}: missing agents/openai.yaml")
    return len(skill_files)


def validate_note_ids(markdown: list[Path], errors: list[str]) -> int:
    ids: dict[str, Path] = {}
    canonical_count = 0
    for path in markdown:
        if TEMPLATES in path.parents:
            continue
        canonical_count += 1
        match = FRONTMATTER_ID.search(path.read_text(encoding="utf-8"))
        if not match:
            errors.append(f"{relative(path)}: missing canonical id")
            continue
        note_id = match.group(1)
        if note_id in ids:
            errors.append(
                f"{relative(path)}: duplicate id {note_id!r}; "
                f"first used by {relative(ids[note_id])}"
            )
        else:
            ids[note_id] = path
    return canonical_count


def validate_wikilinks(markdown: list[Path], errors: list[str]) -> int:
    resolved_files = {path.resolve() for path in markdown}
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for path in markdown:
        by_stem[path.stem].append(path)

    link_count = 0
    for source in markdown:
        text = source.read_text(encoding="utf-8")
        for raw_target in WIKILINK.findall(text):
            link_count += 1
            target = raw_target.strip()
            relative_target = (source.parent / target).with_suffix(".md").resolve()
            if relative_target in resolved_files:
                continue
            stem_matches = by_stem.get(Path(target).stem, [])
            if len(stem_matches) == 1:
                continue
            if len(stem_matches) > 1:
                errors.append(
                    f"{relative(source)}: ambiguous wikilink [[{target}]]"
                )
            else:
                errors.append(f"{relative(source)}: broken wikilink [[{target}]]")
    return link_count


def validate_text_quality(errors: list[str]) -> None:
    roots = [
        ROOT / "AGENTS.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "Makefile",
        ROOT / "README.md",
        ROOT / ".editorconfig",
        ROOT / ".gitattributes",
        ROOT / ".agents",
        ROOT / ".codex",
        ROOT / ".github",
        VAULT,
    ]
    for root in roots:
        paths = [root] if root.is_file() else root.rglob("*")
        for path in paths:
            if not path.is_file() or (
                path.suffix not in {".md", ".toml", ".rules", ".yaml", ".yml"}
                and path.name not in {".editorconfig", ".gitattributes", "Makefile"}
            ):
                continue
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if line.rstrip() != line:
                    errors.append(
                        f"{relative(path)}:{line_number}: trailing whitespace"
                    )


def main() -> int:
    errors: list[str] = []
    markdown, toml_files, json_files = collect_files()
    validate_required_structure(errors)
    validate_serialized(toml_files, json_files, errors)
    skill_count = validate_skills(errors)
    note_count = validate_note_ids(markdown, errors)
    link_count = validate_wikilinks(markdown, errors)
    validate_text_quality(errors)

    if errors:
        print("Workspace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Workspace valid: "
        f"{len(toml_files)} TOML, {len(json_files)} JSON, "
        f"{skill_count} skills, {note_count} canonical notes, "
        f"{len(markdown)} vault markdown files, {link_count} wikilinks."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
