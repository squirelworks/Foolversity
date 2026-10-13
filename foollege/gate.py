"""Import gate.

An import in the chain runs only when the installed build is not the
current stable. If the installed version matches, the dependency is
already current and is left alone.
"""

from __future__ import annotations


def installed(package: str) -> str:
    try:
        from importlib.metadata import version
        return version(package)
    except Exception:
        return ""


def needs_import(package: str, stable: str) -> bool:
    """True only when the installed build is missing or not the stable."""
    return installed(package) != stable
