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

    def test_None(self):
        new = Place()
        new.name = None
        new.description = None
        new.city_id = None
        new.user_id = None
        new.number_rooms = None
        new.number_bathrooms = None
        new.max_guest = None
        new.price_by_night = None
        new.latitude = None
        new.longitude = None
        new.amenities = None
        self.assertIsNone(new.name)
        self.assertIsNone(new.description)
        self.assertIsNone(new.city_id)
        self.assertIsNone(new.user_id)
        self.assertIsNone(new.number_rooms)
        self.assertIsNone(new.number_bathrooms)
        self.assertIsNone(new.max_guest)
        self.assertIsNone(new.price_by_night)
        self.assertIsNone(new.latitude)
        self.assertIsNone(new.longitude)
        self.assertIsNone(new.amenities)


if __name__ == "__main__":
    unittest.main()
