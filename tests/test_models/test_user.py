#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """testing user class"""
    def test_init(self):
        user1 = User()
        user1.first_name = "Ahmed"
        self.assertEqual(user1.first_name, "Ahmed")


if __name__ == "__main__":
    unittest.main()
