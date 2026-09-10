#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def test_module_docstring(self):
        import models.amenity
        self.assertTrue(len(models.amenity.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_default_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_types(self):
        self.assertEqual(str, type(Amenity.name))

    def test_str_representation(self):
        amenity = Amenity()
        self.assertIn("[Amenity]", str(amenity))


if __name__ == "__main__":
    unittest.main()
