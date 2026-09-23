import re
import unittest

from src.session import create, destroy, get


class SessionTests(unittest.TestCase):
    def test_create_returns_a_token(self):
        self.assertRegex(create("alice").token, re.compile(r"^[0-9a-f]{32}$"))

    def test_get_finds_a_live_session(self):
        s = create("bob")
        self.assertEqual(get(s.token).user, "bob")

    def test_destroy_removes_a_session(self):
        s = create("bob")
        destroy(s.token)
        self.assertIsNone(get(s.token))
