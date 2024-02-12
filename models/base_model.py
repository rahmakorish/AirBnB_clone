#!/usr/bin/python3
"""this module represent base class"""
import uuid
import datetime
import json
import models


class BaseModel:
    """class base model"""

    def __init__(self, *args, **kwargs):
        """init function"""
        if kwargs:
            kwargs.pop("__class__")
            for key, v in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    obj = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, obj)
                else:
                    setattr(self, key, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return class object"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, vars(self))

    def save(self):
        """update the update_At attribute"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary of the instance"""
        self.__dict__['__class__'] = __class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return vars(self)
