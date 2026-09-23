import unittest

from src.hash import hash_password, verify


class HashTests(unittest.TestCase):
    def test_hash_is_deterministic(self):
        self.assertEqual(hash_password("x"), hash_password("x"))

    def test_hash_differs_for_different_input(self):
        self.assertNotEqual(hash_password("x"), hash_password("y"))

    def test_verify_accepts_the_right_password(self):
        self.assertTrue(verify("pw", hash_password("pw")))

    def test_verify_rejects_the_wrong_password(self):
        self.assertFalse(verify("nope", hash_password("pw")))
