"""Foollege holds the students.

Foolversity imports Foollege.
Foollege imports Foolcourse, only if the installed build is not the
current stable.
"""

from foollege.file import build, load, write
from foollege.gate import needs_import

# Current stable of Foolcourse.
_FOOLCOURSE_STABLE = "1.0.0r2"

if needs_import("foolcourse", _FOOLCOURSE_STABLE):
    import foolcourse  # noqa: F401

__all__ = ["build", "load", "write"]
