# Overview — Intentions and Purpose

## What Foolversity is

Foolversity is the catalog and administrative layer of a clean-room courseware platform. It generates and manages the files that describe students, schools, and curricula. It does not play books and it does not score quizzes. Those jobs belong to other programs that read the files it writes.

The name is deliberate. Foolversity sits above the course-playing layer the way a university sits above individual courses. It is concerned with knowledge (what is taught) rather than with people (who is taking it). People appear only as the files that enroll them.

## Origin

The platform grew out of reverse-engineering Click2learn / Asymetrix ToolBook II 8.1 courseware (primarily Navy ATT electronics lessons). The original books are 16-bit New Executable (NE) files that run only under Windows 98–XP. The goal was never a perfect binary clone. It was a modern reader that can open the content model those books already carry: pages, objects, OpenScript handlers, and system books.

Foolbook is the reader.  
Foolcourse is the player that catalogs books and launches Foolbook.  
Foolversity is the generator of the enrollment and curriculum files those programs consume.

## Intentions

1. **Clean-room.** No code from the original NE engines is reused. The content model (pages, objects, handlers, system books) is reimplemented from observed behavior and documented formats.
2. **File contract, not shared source.** Foolversity, Foolcourse, and Foolbook are separate repositories. They do not import one another. They meet at well-defined files (`.fcs`, `.curriculum.json`, `.school.json`).
3. **Knowledge, not people.** Foolversity owns the catalog of courseware. Student progress and sessions are a future concern of Foolcollege. Foolversity only writes the files that make enrollment possible.
4. **Backward compatibility where it helps.** Existing ToolBook `.tbk` / `.sbk` books remain openable. New books use `.fbk` / `.fsk`.
5. **Extensibility via system books.** Users change behavior by writing their own system books, the same way ToolBook users did. Core system books load first; user books load after as mods.

## What success looks like

A set of independent programs that, together, let an instructor or institution:

- point at a folder of books,
- declare which of them are official for a curriculum,
- enroll students,
- and have those students open the books and follow the navigation and quiz logic the books already contain,

without needing a Windows 98 virtual machine.
