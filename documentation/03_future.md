# Future Direction

## Server ladder

The intended progression of which program is the server:

1. **Now** — only Foolcourse is a server. Foolbook opens as a native window and does not serve.
2. **Next** — Foollege becomes the server. It runs students (progress, scores, sessions) and hands courses to Foolbook. Foolcollege is the same layer.
3. **Later** — Foolversity becomes the main server above Foollege. It owns the catalog of courseware.

Order: Foolcourse (now) → Foollege → Foolversity.

## Foollege

Foollege holds the students. Foolcollege is the same name, not a second program. The repository is Foollege.

## Platforms

- Desktop: keep `pathlib` + `tkinter`. Prove Windows and macOS.
- Mobile: a separate client (iOS, Android, LineageOS) that talks to the server ladder, fetches book JSON, and renders pages. No local Python, no tkinter. Scaffold exists under `mobile/`; implementation has not started.

## Other open items

- Curriculum maker should accept a path or file picker so the curriculum points at real courseware.
- Enrollment, rostering, and locking of school files.
- Stronger separation between knowledge (Foolversity) and people (Foollege).
- Continued improvement of Foolbook’s geometry: explicit points first, then TBX Vertices, then bounds approximation. The missing original expansion function is a refinement, not a blocker.
- System-book contract: core first, user mods after.

## What is deliberately not in scope

- A binary-compatible clone of the original 16-bit NE engines.
- Running the original ToolBook runtime under a modern Windows.
- Shared source between the three repositories.
