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


if __name__ == "__main__":
    unittest.main()
