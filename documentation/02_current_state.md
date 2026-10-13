# Current State (v1.0.0r2)

## What this version does

Foolversity generates three kinds of files:

- **Student files** (`.fcs`) — Foolcourse Student envelopes.
- **School files** (`.school.json`) — Foolversity’s own school description.
- **Curriculum files** — the JSON that Foolcourse already knows how to read.

It can write them from the command line or from a simple GUI. It can write into a Foolcourse tree (`_student/`, `_curriculum/`) when `--out` is given.

```bash
python3 foolversity
python3 foolversity student alex --name "Alex Kim" --school adin --cohort 2026-A
python3 foolversity school adin --name "Adin" --curriculum "Filing taxes" --student alex
python3 foolversity curriculum "Filing taxes" --official do_i_file --extra phone
python3 foolversity student alex --out /path/to/Foolcourse
```

## Package layout

- `foolversity/` — the package (`student.py`, `school.py`, `curriculum.py`, `fcs.py`, `gui.py`)
- `_schools/` — default location for school files
- `_students/` and `_curricula/` — local placeholders
- `mobile/` — scaffold only (Swift and Kotlin shells over a translated core)
- `documentation/` — this module

## What it does not do

- It does not open books.
- It does not score quizzes.
- It does not serve HTTP.
- It does not enroll, roster, or lock school files (those are later cuts).
- It does not import Foolcourse or Foolbook.

## Known gaps noted in plannedmilestones.md

- Curriculum creation should ask for a path or picker, not only a name.
- Foolbook is a native window; only Foolcourse currently serves.
- tkinter packaging differs across platforms; no Windows/Mac test has been run.
- Mobile is scaffold only.
