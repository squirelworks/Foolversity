"""Foollege file. Holds students."""

from __future__ import annotations

import json
from pathlib import Path


def build(foollege_id: str, name: str = "", students: list[str] | None = None, notes: str = "") -> dict:
    return {
        "id": foollege_id,
        "name": name or foollege_id,
        "students": list(students or []),
        "notes": notes,
    }


def write(path: Path, data: dict) -> Path:
    path = Path(path)
    if not path.name.endswith(".foollege.json"):
        path = path.with_suffix(".foollege.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def load(path: Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    data.setdefault("id", Path(path).stem.split(".")[0])
    data.setdefault("name", data["id"])
    data.setdefault("students", [])
    data.setdefault("notes", "")
    return data
