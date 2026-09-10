#!/usr/bin/python3
"""Creates a unique FileStorage instance shared by the whole app."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
