#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing user class"""
    def test_init(self):
        new = Amenity()
        new.name = "hello"
        self.assertEqual(new.name, "hello")

    def test_None(self):
        newA = Amenity()
        newA.name = None
        self.assertIsNone(newA.name)


if __name__ == "__main__":
    unittest.main()
