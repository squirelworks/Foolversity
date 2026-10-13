"""School file.

Plain JSON for now. A later cut can give it an envelope.

    {
      "id": "nida",
      "name": "Nida",
      "curricula": ["Street sense"],
      "students": ["alex"],
      "notes": ""
    }
"""

from __future__ import annotations

import json
from pathlib import Path


def build(
    school_id: str,
    name: str = "",
    curricula: list[str] | None = None,
    students: list[str] | None = None,
    notes: str = "",
) -> dict:
    return {
        "id": school_id,
        "name": name or school_id,
        "curricula": list(curricula or []),
        "students": list(students or []),
        "notes": notes,
    }


def write(path: Path, data: dict) -> Path:
    path = Path(path)
    if path.suffix.lower() != ".json":
        path = path.with_suffix(".school.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def load(path: Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    data.setdefault("id", Path(path).stem.split(".")[0])
    data.setdefault("name", data["id"])
    data.setdefault("curricula", [])
    data.setdefault("students", [])
    data.setdefault("notes", "")
    return data
