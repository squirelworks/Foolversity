"""Core surface that mobile translates.

Load a book, list pages, show one page. No tkinter. No server.
"""

from __future__ import annotations

import json
from pathlib import Path


def load_book(path: str | Path) -> dict:
    """Return {title, pages: [{id, text, items, quiz}]}."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {
        "title": data.get("title") or Path(path).stem,
        "pages": [
            {
                "id": p.get("id") or "",
                "text": p.get("text") or [],
                "items": p.get("items") or [],
                "quiz": p.get("quiz"),
            }
            for p in data.get("pages") or []
        ],
    }


def page_at(book: dict, index: int) -> dict | None:
    pages = book.get("pages") or []
    if 0 <= index < len(pages):
        return pages[index]
    return None
