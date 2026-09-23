from __future__ import annotations

import hashlib
import hmac


def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()


def verify(pw: str, stored_hash: str) -> bool:
    """Check a plaintext password against a stored hash: verify(password, stored_hash)."""
    a = bytes.fromhex(hash_password(pw))
    b = bytes.fromhex(stored_hash)
    return len(a) == len(b) and hmac.compare_digest(a, b)
