#!/usr/bin/python3
"""
Defines City model and
inherits from BaseMode
"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    state_id = ""
    name = ""
