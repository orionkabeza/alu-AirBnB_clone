#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class."""

    def test_module_docstring(self):
        import models.user
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(User.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_default_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

    def test_str_representation(self):
        user = User()
        self.assertIn("[User]", str(user))


if __name__ == "__main__":
    unittest.main()
