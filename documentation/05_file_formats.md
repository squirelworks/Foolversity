# File Formats and the Contract

Foolversity, Foolcourse, and Foolbook meet at files. They do not share source.

## `.fcs` — Foolcourse Student

Written by Foolversity. Read by Foolcourse and by Foolbook (each has its own opener).

It is an envelope that identifies a student and the school/cohort context. The exact binary or JSON layout is defined by the writer in `foolversity/fcs.py`. Readers must tolerate the format the writer produces; they do not share code.

## `.curriculum.json`

Written by Foolversity. Read by Foolcourse.

Declares a curriculum name, the official course list, and any extra material. Foolcourse uses the official list to decide which courses contribute to the overall score. Extra material is still catalogued and can be opened; it simply does not count toward the total.

## `.school.json`

Written by Foolversity. Read only by Foolversity.

Foolversity’s own description of a school. Foolcourse does not read it.

## Curriculum files Foolcourse already understands

Foolcourse can also load a curriculum file that was produced by its own `--make` tool or by a hand-written JSON of the same shape. Foolversity’s writer produces a compatible file so that a curriculum created here can be dropped into a Foolcourse tree.

## Placement

When `--out` points at a Foolcourse checkout:

- student files go to `_student/`
- curriculum files go to `_curriculum/`
- school files go to `_schools/` beside the Foolversity program unless overridden

## Versioning

The file formats are part of the contract. Changes that break readers require a coordinated release of the affected programs. Because the programs do not share source, the contract is the documentation of the file layout plus the tests that exercise the writer and the known readers.
