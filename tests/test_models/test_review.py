#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """testing user class"""
    def test_init(self):
        new_review = Review()
        new_review.text = "hi"
        self.assertEqual(new_review.text, "hi")


if __name__ == "__main__":
    unittest.main()
