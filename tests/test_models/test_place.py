#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.place import Place
class TestPlace(unittest.TestCase):
    """testing user class"""
        def test_init(self):
            new = Place()
            new.name = "cairo"
            new.description = "pyramids"
            self.assertEqual(new.name, "cairo")
            self.assertEqual(new.description, "pyramids")
if __name__ == "__main__":
    unittest.main()
