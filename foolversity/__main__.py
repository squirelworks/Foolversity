"""Foolversity. Makes the files. Foolcourse reads them.

  python3 -m foolversity                              # open the GUI
  python3 -m foolversity student alex --name "Alex Kim" --school adin
  python3 -m foolversity school adin --name "Adin" --curriculum "Filing taxes" --student alex
  python3 -m foolversity curriculum "Filing taxes" --official do_i_file --extra phone

Commands: student, school, curriculum, gui.
--out PATH   write into a Foolcourse tree (_student/, _curriculum/)
             schools go to _schools/ beside this program unless --out is set
"""

from __future__ import annotations

import sys
from pathlib import Path

_root = Path(__file__).resolve().parents[1]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from foolversity.curriculum import build as build_curriculum, write as write_curriculum
from foolversity.school import build as build_school, write as write_school
from foolversity.student import build as build_student, write as write_student


def main(argv: list[str] | None = None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    if not argv:
        # First launch: ensure a default student and open the GUI
        _ensure_defaults()
        from foolversity.gui import main as gui_main
        return gui_main()
    if argv[0] == "--doctor":
        from foolversity._debug.dump import dump
        path = dump("doctor")
        print(f"Wrote {path}")
        return 0
    if argv[0] == "--freshstart":
        return _freshstart()
    if argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    kind = argv[0]
    rest = argv[1:]
    if kind in ("gui", "--gui"):
        from foolversity.gui import main as gui_main
        return gui_main()
    if kind == "student":
        return _student(rest)
    if kind == "school":
        return _school(rest)
    if kind == "curriculum":
        return _curriculum(rest)
    print(f"unknown: {kind}")
    print("use student, school, or curriculum")
    return 2


def _freshstart() -> int:
    """Force-reinstall this package and its dependency chain."""
    import subprocess
    cmd = [
        sys.executable, "-m", "pip", "install", "--force-reinstall",
        "git+https://github.com/squirelworks/Foolversity.git@v1.0.0r2",
    ]
    return subprocess.call(cmd)


def _ensure_defaults():
    """Create a default student if none exists, so the GUI has something to show."""
    dest = Path(__file__).resolve().parents[1] / "_students"
    dest.mkdir(parents=True, exist_ok=True)
    if any(dest.glob("*.fcs")) or any(dest.glob("*.json")):
        return
    data = build_student("student", name="Student", locale="en")
    write_student(dest / "student", data)
    """Create a default student if none exists, so the GUI has something to show."""
    dest = Path(__file__).resolve().parents[1] / "_students"
    dest.mkdir(parents=True, exist_ok=True)
    if any(dest.glob("*.fcs")) or any(dest.glob("*.json")):
        return
    data = build_student("student", name="Student", locale="en")
    write_student(dest / "student", data)


def _flags(argv: list[str]) -> tuple[list[str], dict]:
    """Split positionals from --key value flags. Repeated flags become lists."""
    pos: list[str] = []
    flags: dict[str, str | list[str]] = {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--") and i + 1 < len(argv):
            key = a[2:].replace("-", "_")
            val = argv[i + 1]
            if key in flags:
                cur = flags[key]
                flags[key] = (cur if isinstance(cur, list) else [cur]) + [val]
            else:
                flags[key] = val
            i += 2
        else:
            pos.append(a)
            i += 1
    return pos, flags


def _out(flags: dict, kind: str) -> Path:
    raw = flags.get("out")
    if isinstance(raw, list):
        raw = raw[-1]
    if raw:
        base = Path(str(raw))
        if kind == "student":
            return base / "_student" if (base / "_courses").exists() or base.name != "_student" else base
        if kind == "curriculum":
            return base / "_curriculum" if base.name != "_curriculum" else base
        if kind == "school":
            return base / "_schools" if base.name != "_schools" else base
        return base
    here = Path(__file__).resolve().parents[1]
    return {"student": here / "_students", "school": here / "_schools", "curriculum": here / "_curricula"}[kind]


def _student(argv: list[str]) -> int:
    pos, flags = _flags(argv)
    if not pos:
        print("student needs an id")
        return 2
    data = build_student(
        pos[0],
        name=str(flags.get("name") or ""),
        preferred_name=str(flags.get("preferred_name") or ""),
        school_id=str(flags.get("school") or ""),
        cohort=str(flags.get("cohort") or ""),
        curriculum=str(flags.get("curriculum") or ""),
        locale=str(flags.get("locale") or "en"),
    )
    path = write_student(_out(flags, "student") / pos[0], data)
    print(path)
    return 0


def _school(argv: list[str]) -> int:
    pos, flags = _flags(argv)
    if not pos:
        print("school needs an id")
        return 2
    curricula = flags.get("curriculum") or []
    students = flags.get("student") or []
    if isinstance(curricula, str):
        curricula = [curricula]
    if isinstance(students, str):
        students = [students]
    data = build_school(
        pos[0],
        name=str(flags.get("name") or ""),
        curricula=curricula,
        students=students,
        notes=str(flags.get("notes") or ""),
    )
    path = write_school(_out(flags, "school") / pos[0], data)
    print(path)
    return 0


def _curriculum(argv: list[str]) -> int:
    pos, flags = _flags(argv)
    if not pos:
        print("curriculum needs a name")
        return 2
    official = flags.get("official") or []
    extras = flags.get("extra") or []
    if isinstance(official, str):
        official = [official]
    if isinstance(extras, str):
        extras = [extras]
    name = pos[0]
    data = build_curriculum(
        name,
        official_name=str(flags.get("official_name") or ""),
        official=official,
        extras=extras,
        root=str(flags.get("root") or "_courses"),
        notes=str(flags.get("notes") or ""),
    )
    path = write_curriculum(_out(flags, "curriculum") / name.replace(" ", "_"), data)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
