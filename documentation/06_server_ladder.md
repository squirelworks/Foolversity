# Server Ladder

## Current (2026-10-13)

Only Foolcourse is a server.  
Foolbook opens as a native window (tkinter) and exits when the window closes. It does not serve.  
Foolversity only generates files.

## Next

Foolcollege becomes the server.

- Runs students: progress, scores, sessions.
- Hands courses to Foolbook.
- Foolcourse continues to exist as the player, but the server role moves up.

## Later

Foolversity becomes the main server above Foolcollege.

- Owns the catalog of courseware.
- Remains concerned with knowledge, not with individual student sessions.
- Student runtime stays in Foolcollege.

## Why the ladder

A browser-based Foolbook does not know when its tab closes, so the process stays up. A native window exits cleanly. Only one program needs to be the long-running server. Moving that role upward keeps each program’s responsibility narrow:

- Foolbook — open a book, run OpenScript, draw.
- Foolcourse — catalog and launch.
- Foolcollege — people and sessions.
- Foolversity — knowledge and catalog.

## Mobile implication

A mobile client will talk to whichever program is currently the server. Today that is Foolcourse. Later it will be Foolcollege, then Foolversity. The protocol is not yet defined; the scaffold under `mobile/` is only a place to put the future client.
