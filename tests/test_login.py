import unittest

from src.login import login


class LoginTests(unittest.TestCase):
    def test_login_accepts_a_valid_password(self):
        s = login("alice", "correct horse battery staple")
        self.assertIsNotNone(s, "expected a session for a valid password")
        self.assertEqual(s.user, "alice")

    def test_login_rejects_a_wrong_password(self):
        self.assertIsNone(login("alice", "wrong"))

    def test_login_rejects_an_unknown_user(self):
        self.assertIsNone(login("mallory", "hunter2"))

    def test_login_rejects_an_empty_password(self):
        self.assertIsNone(login("bob", ""))

    def test_login_is_case_sensitive_on_username(self):
        self.assertIsNone(login("Alice", "correct horse battery staple"))
