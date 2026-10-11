"""Student file generator.

Writes an .fcs with Foolversity's own writer. The envelope is the
Foolcourse Student standard, so Foolcourse can open the file.
This module does not import Foolcourse.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from main.fcs import pack


def blank(student_id: str) -> dict:
    stem = student_id or "student"
    return {
        "id": stem,
        "name": stem.replace("_", " ").title(),
        "preferred_name": "",
        "school_id": "",
        "cohort": "",
        "curriculum": "",
        "locale": "en",
        "theme": "",
        "port": None,
        "enrolled": date.today().isoformat(),
        "started": "",
        "last_seen": "",
        "courses": {},
    }


def build(
    student_id: str,
    name: str = "",
    preferred_name: str = "",
    school_id: str = "",
    cohort: str = "",
    curriculum: str = "",
    locale: str = "en",
) -> dict:
    data = blank(student_id)
    if name:
        data["name"] = name
    if preferred_name:
        data["preferred_name"] = preferred_name
    data["school_id"] = school_id
    data["cohort"] = cohort
    data["curriculum"] = curriculum
    data["locale"] = locale or "en"
    return data


def write(path: Path, data: dict) -> Path:
    path = Path(path)
    if path.suffix.lower() != ".fcs":
        path = path.with_suffix(".fcs")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pack(data))
    return path
