# Foolversity milestones

## Notes

- Curriculum should ask where the curriculum is, not only take a name. The add flow and the CLI both need a path or a picker so the curriculum points at real courseware. [2026-10-13]

- Foolbook should be a native GUI window, not a browser. It exits when the window closes. Only Foolcourse hosts a server, and only to hand a book to the viewer. Browser-based Foolbook does not know when the tab closes, so the process stays up. [2026-10-13]

## Server ladder

Right now only Foolcourse is a server. Foolbook opens on its own as a native window and does not serve.

Later:
- Foolcollege becomes the server (runs students, hands courses to Foolbook).
- Foolversity becomes the main server above that (the catalog of courseware).

Order: Foolcourse (now) -> Foolcollege -> Foolversity. [2026-10-13]
