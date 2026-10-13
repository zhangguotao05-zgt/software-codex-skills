"""Validate the repository's skill packaging; does not run product tests."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = (
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",
    r"\bgithub_pat_[A-Za-z0-9_]{40,}\b",
    r"\bAKIA[A-Z0-9]{16}\b",
)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def load_mapping(text: str, label: str) -> dict:
    value = yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected a YAML mapping")
    return value


def check_skill(path: Path, text: str) -> None:
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0] != "":
        raise ValueError(f"{path}: missing YAML frontmatter")
    metadata = load_mapping(parts[1], str(path))
    name = metadata.get("name")
    if not isinstance(name, str) or name != path.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(f"{path}: name must match its directory in kebab-case")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError(f"{path}: invalid description")
    if len(name) > 64:
        raise ValueError(f"{path}: name exceeds 64 characters")


def validate() -> tuple[int, int]:
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
    )
    files = {ROOT / name for name in output.decode("utf-8").split("\0") if name}
    skill_files = {path for path in files if path.name == "SKILL.md"}
    if not skill_files:
        raise ValueError("No SKILL.md files found")
    for directory in (ROOT / "skills").iterdir():
        if directory.is_dir() and directory / "SKILL.md" not in skill_files:
            raise ValueError(f"{directory.name}: missing SKILL.md")
    for path in sorted(files):
        relative = path.relative_to(ROOT)
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError(f"{relative}: symlinks or external files are not portable")
        if any(part in {".venv", "__pycache__", "node_modules", "artifacts"} for part in relative.parts):
            raise ValueError(f"{relative}: generated content must not be committed")
        if path.name.startswith(".env") or path.suffix.lower() in {".log", ".pem", ".key", ".pfx", ".pyc"}:
            raise ValueError(f"{relative}: local data or credentials must not be committed")
        text = path.read_text(encoding="utf-8")
        if "\ufffd" in text or text.startswith("\ufeff") or "\0" in text:
            raise ValueError(f"{relative}: invalid text encoding")
        if re.search(r"\b[A-Za-z]:[\\/]|(?:^|[\s`])/(?:Users|home)/", text):
            raise ValueError(f"{relative}: machine-specific path")
        if any(re.search(pattern, text) for pattern in SECRET_PATTERNS):
            raise ValueError(f"{relative}: possible credential; inspect locally without printing its value")
        if path in skill_files:
            check_skill(path, text)
        if path.suffix == ".py":
            ast.parse(text, filename=str(relative))
        if path.suffix in {".yaml", ".yml"}:
            mapping = load_mapping(text, str(relative))
            if path.name == "openai.yaml":
                ui = mapping.get("interface", {})
                short = ui.get("short_description", "")
                prompt = ui.get("default_prompt", "")
                skill_name = path.parents[1].name
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    raise ValueError(f"{relative}: invalid UI description")
                if not isinstance(prompt, str) or f"${skill_name}" not in prompt:
                    raise ValueError(f"{relative}: prompt must name its skill")
        if path.suffix == ".md":
            for target in LINK.findall(text):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(ROOT) or resolved not in files:
                    raise ValueError(f"{relative}: reference missing from package: {target}")
    return len(files), len(skill_files)


if __name__ == "__main__":
    try:
        file_count, skill_count = validate()
    except (OSError, ValueError, SyntaxError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {file_count} files, {skill_count} skill; metadata, encoding, references, syntax and content checks")
