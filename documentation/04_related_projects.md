# Related Projects

## Foolbook

The reader. Opens `.fbk` / `.fsk` (native) and `.tbk` / `.sbk` (compatibility). Runs the common OpenScript subset (`go to`, `send`, assignment, `if`/`else`, `step`, `name of`, etc.). Draws polygons that already carry point lists, prefers TBX Vertices when present, and falls back to bounds-based approximations.

Philosophy: discipline in the core path (explicit points → TBX → bounds), deviance in the approximation and in user system books.

Repository: separate from Foolversity. Meets at files only.

## Foolcourse

The player. Catalogs a courses folder, launches Foolbook, and records progress. Official courses (e.g. those under an ATT Master menu) contribute to the overall score; extra material is catalogued but does not count toward the total.

Depends on Foolbook. Does not import Foolversity; it only reads the files Foolversity writes.

## ToolBook reverse-engineering context

The content model came from Navy ATT ToolBook II 8.1 lessons (Click2learn / Asymetrix). The books are 16-bit NE files with a JBO signature after a PE stub. Pages are marked by a specific object header; widgets are nested property blocks. OpenScript handlers are compressed bytecode that has been decoded.

Key technical notes that shaped the clean-room design:

- The original painters live in TB80BAS.DLL (and related DLLs). They read 14 00 00 records and call GDI.
- Many shapes are stored as bounds only; the original runtime expands them. Foolbook prefers explicit geometry and falls back to approximation.
- System books (`.sbk`) are resource containers, not script books. Logic for trainers and sessions lives in companion DLLs (`nc81int.dll`, `nc81rec.dll`).
- The modern stack deliberately does not try to host the original NE images. Unicorn and SoftICE work remains available for investigation but is not part of the runtime path.

## Other repositories in the family

- toolbookunpacker — honest NE unpacker for the original OPTLOADER-protected binaries.
- TBpipeline — experimental host that reaches a page without a full Win98 environment.
- TBWorldview — printable documentation of the reverse-engineering work.

None of these are imported by Foolversity.

## Research notes (2026-10-14)

- RTM triage and nameable functions filed at `tbworkingpapers/tbwp0018/`.
- Object struct layout and palette requirement filed at `Foolbook/documentation/research-notes.md`.

## RTM research (2026-10-14)

TB80RTM is UI and memory management heavy. No named file open. Named CDB functions: `CDBSAVEBOOK`, `CDBGETVALUEEX`, `CDBSENDVALUEEX`, `CDBSETVALUEEX`.

`FUN_1068_0098` is a `GLOBALALLOC` wrapper with retry on OOM. `FUN_1068_00d0` shows the OOM dialog. `FUN_1068_0000` is the dialog helper. `FUN_10d0_3166` is the window long reader.

Object struct is 0x76 bytes. Bounds at `+0x0f`. GDI handle at `+0x3b`. BitBlt flag at `+0x1f`. Point count at `+0x30`, point array at `+0x32`.

8bpp BMPs need the book's palette from BAS segment 1150.
