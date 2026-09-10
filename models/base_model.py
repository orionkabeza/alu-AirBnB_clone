#!/usr/bin/python3
"""Defines the BaseModel class, the parent of all other model classes."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines common attributes/methods used by all AirBnB classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance, or rebuild one from kwargs.

        Args:
            *args: not used.
            **kwargs: attribute names and values, used to recreate an
                instance from its dictionary representation. If empty,
                a brand new instance is created instead.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            now = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime and persist."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        The returned dictionary includes a __class__ key with the
        class name, and has created_at/updated_at as ISO format
        strings instead of datetime objects.
        """
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
