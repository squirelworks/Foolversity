# Foolversity milestones

## Notes

- Curriculum should ask where the curriculum is, not only take a name. The add flow and the CLI both need a path or a picker so the curriculum points at real courseware. [2026-10-13]

- Foolbook should be a native GUI window, not a browser. It exits when the window closes. Only Foolcourse hosts a server, and only to hand a book to the viewer. Browser-based Foolbook does not know when the tab closes, so the process stays up. [2026-10-13]

## Server ladder

Right now only Foolcourse is a server. Foolbook opens on its own as a native window and does not serve.

Later:
- Foollege becomes the server (runs students, hands courses to Foolbook). Foolcollege is the same layer.
- Foolversity becomes the main server above that (the catalog of courseware).

Order: Foolcourse (now) -> Foollege -> Foolversity. Foolcollege is Foollege, not a second program. [2026-10-27]

## Platforms

Foolversity, Foolcourse, and Foolbook use pathlib and tkinter. No hardcoded Linux paths. They should run on Windows and Mac if Python includes tkinter.

Known gaps, not yet fixed:
- tkinter is a separate package on some Linux distros (python3-tk). Windows and Mac installers usually include it.
- --freshstart shells out to pip. Works on all three if pip is on PATH.
- No platform test has been run on Windows or Mac. [2026-10-13]

## Mobile

Does not run on iOS, Android, or LineageOS. tkinter is desktop only.

Scaffold, not built:
- A mobile client would be a separate app that talks to the Foolcourse (later Foollege, then Foolversity) server.
- It would fetch the book JSON and render pages, text, and buttons. No local Python, no tkinter.
- LineageOS is Android. Same client as Android.
- iOS needs its own build. Same protocol.

Not started. [2026-10-13]
