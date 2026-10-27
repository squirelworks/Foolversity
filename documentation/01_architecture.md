# Architecture and Hierarchy

## The stack

```
Foolversity   holds the courses
Foollege      holds the students
Foolcourse    holds the instruction
Foolbook      opens the book
```

A curriculum is figured out on its own.
OpenScript lets an old ToolBook be reused.

Supporting programs (separate repositories):

- **Foolcourse** — the player. Catalogs a courses folder, launches Foolbook, records progress.
- **Foolbook** — the reader. Opens a book (`.fbk`, `.tbk`, `.fsk`, `.sbk`), runs the common OpenScript subset, draws what it can.
- **Foollege** — holds the students. Foolcollege is the same layer, not another program. It is not a running server yet. When it is, it runs progress, scores, and sessions, and hands courses to Foolbook.
- **Foolversity** (this project) — writes the files that describe students, schools, and curricula. Later becomes the main server above Foollege.

## Boundaries

Foolversity, Foolcourse, and Foolbook do not import one another. They meet at files.

| File | Writer | Readers |
|------|--------|---------|
| `.fcs` (Foolcourse Student) | Foolversity | Foolcourse, Foolbook (each with its own opener) |
| `.curriculum.json` | Foolversity | Foolcourse |
| `.school.json` | Foolversity | Foolversity |

See `STANDARD.md` in the repository root for the exact contract.

## Foollege

Foollege holds the students. A `.foollege.json` names them.
It does not hold courses. Foolversity holds the courses.
It does not hold the instruction. Foolcourse holds that.

## System books

Load order is fixed:

1. Core system books (shipped with Foolbook) load first.
2. User system books load after, as mods.

A user book may override a handler, replace a shape approximation, or add a new one. It cannot remove the core. This is the same discipline/deviance model used inside Foolbook itself: the core path is strict; the approximation and the user file are where variation is allowed.

## Platforms

Current code uses `pathlib` and `tkinter`. It is intended to run on Windows, macOS, and Linux (where Python’s tkinter package is installed). No platform-specific tests have been run yet.

Mobile (iOS, Android, LineageOS) is not supported by the desktop programs. A separate client that talks to the server ladder is scaffolded under `mobile/` but not built.
