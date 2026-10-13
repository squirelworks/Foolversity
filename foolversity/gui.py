"""Foolversity window.

  python3 foolversity gui

Three forms. Each writes the same file the matching CLI command writes.
"""

from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from foolversity.curriculum import build as build_curriculum, write as write_curriculum
from foolversity.school import build as build_school, write as write_school
from foolversity.student import build as build_student, write as write_student


def main() -> int:
    root = tk.Tk()
    root.title("Foolversity")
    root.geometry("520x360")
    nb = ttk.Notebook(root)
    nb.pack(fill="both", expand=True, padx=8, pady=8)
    _student_tab(nb)
    _school_tab(nb)
    _curriculum_tab(nb)
    root.mainloop()
    return 0


def _row(parent, label, var):
    line = ttk.Frame(parent)
    line.pack(fill="x", pady=2)
    ttk.Label(line, text=label, width=14).pack(side="left")
    ttk.Entry(line, textvariable=var).pack(side="left", fill="x", expand=True)


def _student_tab(nb):
    f = ttk.Frame(nb, padding=8)
    nb.add(f, text="Student")
    sid, name, school, cohort = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
    _row(f, "Id", sid)
    _row(f, "Name", name)
    _row(f, "School", school)
    _row(f, "Cohort", cohort)
    out = tk.StringVar(value=str(Path.cwd()))

    def go():
        if not sid.get().strip():
            messagebox.showwarning("Foolversity", "Student needs an id")
            return
        dest = Path(out.get()) / "_student" / sid.get().strip()
        path = write_student(dest, build_student(
            sid.get().strip(), name.get().strip(), school.get().strip(),
            cohort=cohort.get().strip(),
        ))
        messagebox.showinfo("Foolversity", f"Wrote {path}")

    ttk.Button(f, text="Write student", command=go).pack(anchor="w", pady=8)


def _school_tab(nb):
    f = ttk.Frame(nb, padding=8)
    nb.add(f, text="School")
    sid, name, curricula, students = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
    _row(f, "Id", sid)
    _row(f, "Name", name)
    _row(f, "Curricula", curricula)
    _row(f, "Students", students)

    def go():
        if not sid.get().strip():
            messagebox.showwarning("Foolversity", "School needs an id")
            return
        dest = Path(__file__).resolve().parents[1] / "_schools" / sid.get().strip()
        path = write_school(dest, build_school(
            sid.get().strip(), name.get().strip(),
            curricula=[s.strip() for s in curricula.get().split(",") if s.strip()],
            students=[s.strip() for s in students.get().split(",") if s.strip()],
        ))
        messagebox.showinfo("Foolversity", f"Wrote {path}")

    ttk.Button(f, text="Write school", command=go).pack(anchor="w", pady=8)


def _curriculum_tab(nb):
    f = ttk.Frame(nb, padding=8)
    nb.add(f, text="Curriculum")
    name, official, extras = tk.StringVar(), tk.StringVar(), tk.StringVar()
    _row(f, "Name", name)
    _row(f, "Official ids", official)
    _row(f, "Extra ids", extras)

    def go():
        if not name.get().strip():
            messagebox.showwarning("Foolversity", "Curriculum needs a name")
            return
        dest = Path(__file__).resolve().parents[1] / "_curricula" / name.get().strip().replace(" ", "_")
        path = write_curriculum(dest, build_curriculum(
            name.get().strip(),
            official=[s.strip() for s in official.get().split(",") if s.strip()],
            extras=[s.strip() for s in extras.get().split(",") if s.strip()],
        ))
        messagebox.showinfo("Foolversity", f"Wrote {path}")

    ttk.Button(f, text="Write curriculum", command=go).pack(anchor="w", pady=8)
