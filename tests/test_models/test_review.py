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

    def test_none(self):
        new_review = Review()
        new_review.text = None
        new_review.place_id = None
        new_review.user_id = None
        self.assertIsNone(new_review.text)
        self.assertIsNone(new_review.user_id)
        self.assertIsNone(new_review.place_id)


if __name__ == "__main__":
    unittest.main()
