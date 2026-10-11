"""Curriculum file.

The same shape Foolcourse reads. Official courses count toward the
overall. Anything else is extra.
"""

from __future__ import annotations

import json
from pathlib import Path


def build(
    name: str,
    official_name: str = "",
    official: list[str] | None = None,
    extras: list[str] | None = None,
    root: str = "_courses",
    notes: str = "",
) -> dict:
    return {
        "name": name,
        "official_name": official_name or name,
        "official": list(official or []),
        "extras": list(extras or []),
        "root": root,
        "notes": notes,
    }


def write(path: Path, data: dict) -> Path:
    path = Path(path)
    if not path.name.endswith(".curriculum.json"):
        path = path.with_suffix(".curriculum.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path
