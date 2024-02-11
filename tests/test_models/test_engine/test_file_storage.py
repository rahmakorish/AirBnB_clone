#!/usr/bin/python3
"""this module test user class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """testing user class"""
    def test_init(self):
        newstorage = FileStorage()
        newstorage.__file_path = "file1.json"
        self.assertEqual(newstorage.__file_path, "file1.json")


if __name__ == "__main__":
    unittest.main()
