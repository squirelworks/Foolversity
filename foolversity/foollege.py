"""Foollege file.

A foollege sits under Foolversity and owns foolcourses.
A foolcourse holds foolbooks. A foolbook can use OpenScript.

Plain JSON. Foolcourse reads the same shape with its own loader.

    {
      "id": "money",
      "name": "Money",
      "courses": ["do_i_file", "papers"],
      "notes": ""
    }
"""

from __future__ import annotations

import json
from pathlib import Path


def build(
    foollege_id: str,
    name: str = "",
    courses: list[str] | None = None,
    notes: str = "",
) -> dict:
    return {
        "id": foollege_id,
        "name": name or foollege_id,
        "courses": list(courses or []),
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
    data.setdefault("courses", [])
    data.setdefault("notes", "")
    return data
