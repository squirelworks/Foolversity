"""Foollege holds the students.

Foolversity imports Foollege.
Foollege imports Foolcourse.
"""

from foollege.file import build, load, write

# Foolcourse holds the instruction. Import it so the chain is real.
import foolcourse  # noqa: F401

__all__ = ["build", "load", "write"]
