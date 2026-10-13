"""Foolversity writer for a Foolcourse Student file.

This is Foolversity's code. It does not import Foolcourse.
It writes the .fcs envelope described by the Foolcourse Student standard:

    FCS1            magic
    1 byte          version (1)
    16 bytes        salt
    12 bytes        nonce
    rest            AES-GCM ciphertext of the UTF-8 JSON

The password is recovered here, not stored as text. A file written by
this module can be opened by Foolcourse's own opener.
"""

from __future__ import annotations

import json
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

MAGIC = b"FCS1"
VERSION = 1
ROUNDS = 200_000

# Rebuilt by this writer. Not the Foolcourse opener, same recovered value.
_ORIGIN = 0x28
_OFF = (45, 79, 45)


def _password() -> str:
    return "".join(chr(_ORIGIN + n) for n in _OFF)


def pack(data: dict, password: str | None = None) -> bytes:
    """Encrypt a student dict into an .fcs blob."""
    password = password or _password()
    body = json.dumps(data, indent=2).encode("utf-8")
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = _derive(password, salt)
    sealed = AESGCM(key).encrypt(nonce, body, MAGIC)
    return MAGIC + bytes([VERSION]) + salt + nonce + sealed


def _derive(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ROUNDS,
    )
    return kdf.derive(password.encode("utf-8"))
