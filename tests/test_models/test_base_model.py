#!/usr/bin/python3
"""this module represent base class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testing base model"""
    def test_init(self):
        new = BaseModel()
        new.name = "rahma"
        new.my_number = 1
        self.assertEqual(new.name, "rahma")
        self.assertEqual(new.my_number, 1)

    def test_inistance(self):
        new = BaseModel()
        self.assertIsInstance(new, BaseModel)

    def SetUp(self):
        new_model = Basemodel()
        stringform = "[BaseModel] (1) {'id':1}"
        self.asserEqual(str(new_model), stringform)


if __name__ == "__main__":
    unittest.main()
