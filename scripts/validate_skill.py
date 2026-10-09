#!/usr/bin/env python3
"""Validate the text-only image Skill structure without external dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE.md",
    "CONTRIBUTING.md",
    "references/mode-1-zine.md",
    "references/mode-2-ink-postcard.md",
    "references/mode-3-surreal-pop.md",
    "references/mode-4-second-world.md",
    "references/quality-gates.md",
    "examples/usage-examples.md",
]
errors = []
for rel in REQUIRED:
    path = ROOT / rel
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"Missing/empty: {rel}")

if (ROOT / "SKILL.md").exists():
    s = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not s.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    if not re.search(r"(?m)^name:\s*scene-image-style-composer\s*$", s):
        errors.append("SKILL.md frontmatter requires the correct name")
    if not re.search(r"(?m)^description:\s*", s):
        errors.append("SKILL.md needs a description")
    for name in ["mode-1-zine.md", "mode-2-ink-postcard.md", "mode-3-surreal-pop.md", "mode-4-second-world.md", "quality-gates.md"]:
        if name not in s:
            errors.append(f"SKILL.md does not reference {name}")

for f in ROOT.rglob("*"):
    if f.is_file():
        if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".heic", ".psd"}:
            errors.append(f"Unexpected binary image in text-only skill: {f.relative_to(ROOT)}")
        if f.stat().st_size > 400_000:
            errors.append(f"Unexpected large file: {f.relative_to(ROOT)}")

if errors:
    print("Skill validation FAILED:\n - " + "\n - ".join(errors))
    sys.exit(1)
print("Skill validation passed: four modes, references and publication files present.")
