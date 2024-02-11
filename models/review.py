#!/usr/bin/python3
"""
Defines review model and inherits
from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""

