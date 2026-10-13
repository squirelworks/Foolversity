"""Foolversity window.

Lists of students, schools, and curricula. Add new ones from each tab.
"""

from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

from foolversity.curriculum import build as build_curriculum, write as write_curriculum
from foolversity.school import build as build_school, write as write_school
from foolversity.student import build as build_student, write as write_student


def _dir(kind: str) -> Path:
    here = Path(__file__).resolve().parents[1]
    name = {"student": "_students", "school": "_schools", "curriculum": "_curricula"}[kind]
    dest = here / name
    dest.mkdir(parents=True, exist_ok=True)
    return dest


def _list_files(kind: str) -> list[str]:
    d = _dir(kind)
    return sorted(p.stem for p in d.iterdir() if p.suffix in (".fcs", ".json", ".fsk"))


def main() -> int:
    root = tk.Tk()
    root.title("Foolversity")
    root.geometry("480x400")
    nb = ttk.Notebook(root)
    nb.pack(fill="both", expand=True, padx=8, pady=8)
    _tab(nb, "Students", "student", _add_student)
    _tab(nb, "Schools", "school", _add_school)
    _tab(nb, "Curricula", "curriculum", _add_curriculum)
    root.mainloop()
    return 0


def _tab(nb, title, kind, add_fn):
    f = ttk.Frame(nb, padding=8)
    nb.add(f, text=title)
    # Button first so it stays visible
    bar = ttk.Frame(f)
    bar.pack(fill="x", side="bottom")
    lb = tk.Listbox(f)
    lb.pack(fill="both", expand=True, side="top")
    for name in _list_files(kind):
        lb.insert("end", name)

    def refresh():
        lb.delete(0, "end")
        for name in _list_files(kind):
            lb.insert("end", name)

    def add():
        add_fn()
        refresh()

    ttk.Button(bar, text=f"Add {kind}", command=add).pack(side="left", pady=6)


def _add_student():
    sid = simpledialog.askstring("New student", "Id")
    if not sid:
        return
    name = simpledialog.askstring("New student", "Name") or sid
    write_student(_dir("student") / sid.strip(), build_student(sid.strip(), name=name.strip()))


def _add_school():
    sid = simpledialog.askstring("New school", "Id")
    if not sid:
        return
    name = simpledialog.askstring("New school", "Name") or sid
    write_school(_dir("school") / sid.strip(), build_school(sid.strip(), name=name.strip()))


def _add_curriculum():
    name = simpledialog.askstring("New curriculum", "Name")
    if not name:
        return
    write_curriculum(
        _dir("curriculum") / name.strip().replace(" ", "_"),
        build_curriculum(name.strip()),
    )
