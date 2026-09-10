#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import time
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests that BaseModel and its methods have documentation."""

    def test_module_docstring(self):
        """Test that the module has a docstring."""
        import models.base_model
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_class_docstring(self):
        """Test that the BaseModel class has a docstring."""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docstrings(self):
        """Test that every BaseModel method has a docstring."""
        methods = ["__init__", "__str__", "save", "to_dict"]
        for name in methods:
            method = getattr(BaseModel, name)
            self.assertTrue(len(method.__doc__) > 0)


class TestBaseModelInit(unittest.TestCase):
    """Tests the creation of new BaseModel instances."""

    def test_id_is_string(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))

    def test_two_instances_have_different_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_is_datetime(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.created_at))

    def test_updated_at_is_datetime(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.updated_at))

    def test_created_at_and_updated_at_start_equal(self):
        bm = BaseModel()
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_args_not_used(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_kwargs_rebuild(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="1234", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "1234")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_kwargs_skips_class_key(self):
        bm = BaseModel(**{"__class__": "SomethingElse"})
        self.assertNotEqual(bm.__class__.__name__, "SomethingElse")
        self.assertEqual(bm.__class__.__name__, "BaseModel")


class TestBaseModelStr(unittest.TestCase):
    """Tests the string representation of a BaseModel instance."""

    def test_str_format(self):
        bm = BaseModel()
        expected = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected)


class TestBaseModelSave(unittest.TestCase):
    """Tests the save method of BaseModel."""

    def test_save_updates_updated_at(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        time.sleep(0.01)
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)
        self.assertGreater(bm.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        bm = BaseModel()
        old_created_at = bm.created_at
        bm.save()
        self.assertEqual(old_created_at, bm.created_at)


class TestBaseModelToDict(unittest.TestCase):
    """Tests the to_dict method of BaseModel."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        d = bm.to_dict()
        for key in ("id", "created_at", "updated_at", "__class__"):
            self.assertIn(key, d)

    def test_to_dict_datetimes_are_strings(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_to_dict_class_value(self):
        bm = BaseModel()
        self.assertEqual(bm.to_dict()["__class__"], "BaseModel")

    def test_to_dict_exact_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        expected = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(bm.to_dict(), expected)

    def test_to_dict_does_not_mutate_instance(self):
        bm = BaseModel()
        bm.to_dict()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict_with_extra_attribute(self):
        bm = BaseModel()
        bm.name = "My First Model"
        bm.number = 89
        d = bm.to_dict()
        self.assertEqual(d["name"], "My First Model")
        self.assertEqual(d["number"], 89)

    def test_to_dict_then_recreate(self):
        bm = BaseModel()
        bm.name = "Test"
        new_bm = BaseModel(**bm.to_dict())
        self.assertEqual(bm.id, new_bm.id)
        self.assertEqual(bm.created_at, new_bm.created_at)
        self.assertEqual(bm.name, new_bm.name)
        self.assertIsNot(bm, new_bm)


if __name__ == "__main__":
    unittest.main()
