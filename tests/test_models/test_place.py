#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests the Place class."""

    def test_module_docstring(self):
        import models.place
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(Place.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_default_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attribute_types(self):
        self.assertEqual(str, type(Place.city_id))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.max_guest))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))

    def test_str_representation(self):
        place = Place()
        self.assertIn("[Place]", str(place))


if __name__ == "__main__":
    unittest.main()
