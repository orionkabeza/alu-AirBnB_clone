#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review left on a place.

    Attributes:
        place_id (str): the id of the Place being reviewed.
        user_id (str): the id of the User who wrote the review.
        text (str): the content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
