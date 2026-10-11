#!/usr/bin/env python3
"""Foolversity launcher. See main/__main__.py."""

import sys
from pathlib import Path

_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from main.__main__ import main

if __name__ == "__main__":
    raise SystemExit(main())
