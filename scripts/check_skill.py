#!/usr/bin/env python3
"""Validate the paper-review-and-revise skill before it is packaged.

Checks the SKILL.md frontmatter, the version in CITATION.cff, the venue
profile template, every venue profile, and the relative links in the
Markdown files.

Run it from anywhere inside the repository:

    python3 scripts/check_skill.py

It needs PyYAML (pip install pyyaml).
"""

import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "LICENSE",
    "README.md",
    "PROMPT.md",
    "CITATION.cff",
    "field-checklists.md",
    "venues/README.md",
    "venues/_template.yaml",
    "venues/publishers.md",
    "venues/lists/geotechnical-offshore.md",
]

SKILL_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}

PROFILE_KEYS = {
    "name", "also_known_as", "type", "publisher", "fields", "issn",
    "links", "templates", "notes", "last_checked",
}
PROFILE_TYPES = {
    "journal", "journal-family", "conference", "book-series",
    "thesis", "preprint-server", "other",
}
MAIN_LINKS = ("homepage", "author_guidelines", "call_for_papers")
PROFILE_FILE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*\.yaml")
ISSN = re.compile(r"\d{4}-\d{3}[\dX]")
MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)\)")

problems = []


def report(where, message):
    problems.append(f"{where}: {message}")


def read_yaml(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        report(path.relative_to(ROOT).as_posix(), f"YAML error: {exc}")
        return None


def check_required_files():
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            report(rel, "required file is missing")


def check_skill_md():
    """Return the version in the SKILL.md metadata, or None."""
    path = ROOT / "SKILL.md"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        report("SKILL.md", "the file must open with YAML frontmatter between --- lines")
        return None
    try:
        front = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        report("SKILL.md", f"frontmatter YAML error: {exc}")
        return None
    if not isinstance(front, dict):
        report("SKILL.md", "the frontmatter must be a mapping")
        return None

    unknown = set(front) - SKILL_KEYS
    if unknown:
        report("SKILL.md", f"unexpected frontmatter keys: {sorted(unknown)}")

    name = front.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        report("SKILL.md", "name must be lowercase words joined by hyphens, at most 64 characters")

    description = front.get("description")
    if not isinstance(description, str) or not description.strip():
        report("SKILL.md", "description is missing")
    else:
        if len(description) > 1024:
            report("SKILL.md", f"description has {len(description)} characters; the limit is 1024")
        if "<" in description or ">" in description:
            report("SKILL.md", "description must not contain angle brackets")

    metadata = front.get("metadata") or {}
    version = metadata.get("version") if isinstance(metadata, dict) else None
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        report("SKILL.md", "metadata.version must be a quoted version such as \"2.0.0\"")
        return None
    return version


def check_citation(version):
    path = ROOT / "CITATION.cff"
    if not path.is_file() or version is None:
        return
    data = read_yaml(path)
    if not isinstance(data, dict):
        report("CITATION.cff", "must be a YAML mapping")
        return
    if str(data.get("version")) != version:
        report("CITATION.cff", f"version {data.get('version')} differs from the SKILL.md version {version}")


def normalise(label):
    text = unicodedata.normalize("NFKD", label).encode("ascii", "ignore").decode()
    text = " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())
    return re.sub(r"^the ", "", text)


def string_list(where, key, value):
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        report(where, f"{key} must be a list of non-empty text items")
        return []
    return value


def link_map(where, key, value, required):
    if value is None:
        if required:
            report(where, f"{key} is required")
        return {}
    if not isinstance(value, dict):
        report(where, f"{key} must be a mapping of names to links")
        return {}
    links = {}
    for name, url in value.items():
        if url in (None, ""):
            continue
        if not isinstance(url, str) or not url.startswith("https://") or any(ch.isspace() for ch in url):
            report(where, f"{key}.{name} must be a single https:// link")
            continue
        links[name] = url
    return links


def check_template():
    path = ROOT / "venues" / "_template.yaml"
    if not path.is_file():
        return
    data = read_yaml(path)
    if not isinstance(data, dict):
        report("venues/_template.yaml", "must be a YAML mapping")
        return
    if set(data) != PROFILE_KEYS:
        report("venues/_template.yaml", "must list exactly the profile keys")


def check_profiles():
    folder = ROOT / "venues" / "profiles"
    files = sorted(path for path in folder.glob("*") if path.is_file())
    if not files:
        report("venues/profiles", "no venue profiles found")
    owners = {}
    for path in files:
        where = path.relative_to(ROOT).as_posix()
        if not PROFILE_FILE.fullmatch(path.name):
            report(where, "file names use lowercase letters, digits and hyphens, and end in .yaml")
            continue
        data = read_yaml(path)
        if data is None:
            continue
        if not isinstance(data, dict):
            report(where, "a profile must be a YAML mapping")
            continue

        unknown = set(data) - PROFILE_KEYS
        if unknown:
            report(where, f"unknown keys: {sorted(unknown)}; see venues/_template.yaml")

        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            report(where, "name is required")
            name = None
        if data.get("type") not in PROFILE_TYPES:
            report(where, f"type must be one of: {', '.join(sorted(PROFILE_TYPES))}")
        publisher = data.get("publisher")
        if publisher is not None and not (isinstance(publisher, str) and publisher.strip()):
            report(where, "publisher must be non-empty text")

        aliases = string_list(where, "also_known_as", data.get("also_known_as"))
        string_list(where, "fields", data.get("fields"))
        string_list(where, "notes", data.get("notes"))
        for issn in string_list(where, "issn", data.get("issn")):
            if not ISSN.fullmatch(issn):
                report(where, f"ISSN {issn!r} must be written as NNNN-NNNN")

        links = link_map(where, "links", data.get("links"), required=True)
        if not any(key in links for key in MAIN_LINKS):
            report(where, "links needs at least one of homepage, author_guidelines or call_for_papers")
        link_map(where, "templates", data.get("templates"), required=False)

        checked = data.get("last_checked")
        if isinstance(checked, str):
            try:
                checked = dt.date.fromisoformat(checked)
            except ValueError:
                checked = None
        if not isinstance(checked, dt.date):
            report(where, "last_checked must be a date written as YYYY-MM-DD")

        for label in ([name] if name else []) + aliases:
            key = normalise(label)
            if key in owners and owners[key] != where:
                report(where, f"the name or alias {label!r} is already used in {owners[key]}")
            owners.setdefault(key, where)
    return len(files)


def check_markdown_links():
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        for target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            if not (path.parent / target.split("#")[0]).exists():
                report(rel.as_posix(), f"link to {target} points to nothing")


def main():
    check_required_files()
    version = check_skill_md()
    check_citation(version)
    check_template()
    count = check_profiles()
    check_markdown_links()
    if problems:
        print(f"{len(problems)} problem(s) found:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"All checks passed: SKILL.md version {version}, {count} venue profiles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
