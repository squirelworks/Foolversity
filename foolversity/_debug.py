"""Foolversity diagnostics.

  python3 -m foolversity --doctor
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


def run() -> int:
    print("Foolversity doctor")
    print(f"  python: {sys.version.split()[0]}")
    print(f"  executable: {sys.executable}")
    here = Path(__file__).resolve().parent
    print(f"  package: {here}")
    for name in ("foolversity", "foolcourse", "foolbook", "openscript_analysis"):
        try:
            mod = importlib.import_module(name)
            loc = getattr(mod, "__file__", "?")
            print(f"  {name}: ok  {loc}")
        except Exception as e:
            print(f"  {name}: FAIL  {e}")
    students = here.parent / "_students"
    print(f"  students dir: {students}  exists={students.exists()}")
    return 0
