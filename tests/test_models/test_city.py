#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def test_module_docstring(self):
        import models.city
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(City.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_types(self):
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))

    def test_str_representation(self):
        city = City()
        self.assertIn("[City]", str(city))


if __name__ == "__main__":
    unittest.main()
