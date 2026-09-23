from __future__ import annotations

import secrets
import time
from dataclasses import dataclass


@dataclass
class Session:
    user: str
    token: str
    created_at: float


_sessions: dict[str, Session] = {}


def create(user: str) -> Session:
    s = Session(user=user, token=secrets.token_hex(16), created_at=time.time())
    _sessions[s.token] = s
    return s


def get(token: str) -> Session | None:
    return _sessions.get(token)


def destroy(token: str) -> bool:
    return _sessions.pop(token, None) is not None
