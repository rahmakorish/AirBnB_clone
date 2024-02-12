#!/usr/bin/python3
"""this module test state class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """testing base model"""
    def test_init(self):
        new_state = State()
        new_state.name = "Alexandria"
        self.assertEqual(new_state.name, "Alexandria")
        newstate = State()
        newstate.name = None
        self.assertEqual(newstate.name, None)


if __name__ == "__main__":
    unittest.main()
