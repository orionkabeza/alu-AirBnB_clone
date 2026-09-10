#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the Review class."""

    def test_module_docstring(self):
        import models.review
        self.assertTrue(len(models.review.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(Review.__doc__) > 0)

    def test_is_subclass_of_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_types(self):
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_str_representation(self):
        review = Review()
        self.assertIn("[Review]", str(review))


if __name__ == "__main__":
    unittest.main()
