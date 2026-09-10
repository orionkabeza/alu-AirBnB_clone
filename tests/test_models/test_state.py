#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests the State class."""

    def test_module_docstring(self):
        import models.state
        self.assertTrue(len(models.state.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(State.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_default_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_types(self):
        self.assertEqual(str, type(State.name))

    def test_str_representation(self):
        state = State()
        self.assertIn("[State]", str(state))


if __name__ == "__main__":
    unittest.main()
