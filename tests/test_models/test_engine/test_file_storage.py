#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage engine."""

    def setUp(self):
        """Keep a copy of __objects so tests don't affect each other."""
        self.backup = FileStorage._FileStorage__objects.copy()

    def tearDown(self):
        """Restore __objects and remove any file created by a test."""
        FileStorage._FileStorage__objects = self.backup
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_module_docstring(self):
        import models.engine.file_storage as fs
        self.assertTrue(len(fs.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_all_returns_dict(self):
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object_with_correct_key(self):
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], bm)

    def test_save_writes_json_file(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path) as f:
            data = json.load(f)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, data)

    def test_reload_rebuilds_objects(self):
        bm = BaseModel()
        bm.name = "Reload Test"
        storage.new(bm)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Reload Test")

    def test_reload_no_file_does_not_raise(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        try:
            storage.reload()
        except Exception:
            self.fail("reload() raised an exception with no file present")


if __name__ == "__main__":
    unittest.main()
