#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """testing user class"""
    def test_init(self):
        new_city = City()
        new_city.name = "maadi"
        self.assertEqual(new_city.name, "maadi")

    def test_None(self):
        new = City()
        new.name = None
        new.state_id = None
        self.assertIsNone(new.name)
        self.assertIsNone(new.state_id)


if __name__ == "__main__":
    unittest.main()
