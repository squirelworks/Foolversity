# Mobile scaffold

The desktop app is Python. Mobile does not run it directly.
Each native shell calls the same core, translated.

## Translation

The core that mobile needs is small:

- load a book (JSON)
- list pages
- show a page (text, items, quiz)
- record progress

`shared/core.py` is that surface. A build step translates it:

- iOS: Python to Swift, or embed via a bridge
- Android: Python to Kotlin, or embed via Chaquopy

The shells below are stubs. They show the call shape.
They do not build or run.
