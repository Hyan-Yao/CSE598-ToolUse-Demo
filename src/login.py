from __future__ import annotations

from dataclasses import dataclass

from src.hash import hash_password, verify
from src.session import Session, create


@dataclass
class User:
    name: str
    hash: str


_users: dict[str, User] = {
    "alice": User(name="alice", hash=hash_password("correct horse battery staple")),
    "bob": User(name="bob", hash=hash_password("hunter2")),
}


def login(username: str, pw: str) -> Session | None:
    user = _users.get(username)
    if user is None or not pw:
        return None
    if not verify(user.hash, pw):
        return None
    return create(user.name)
