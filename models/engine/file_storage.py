#!/usr/bin/python3
import json 
import uuid
import datetime

"""this module  serializes instances to a JSON file and deserializes JSON file to instances"""


class FileStorage:
    """class to serialize and deserialize"""
        __file_path= "./file.json"
        __objects={}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj): 
        """sets in __objects the obj with key <obj class name>.id"""
        #objecty = 
        pass

    def save(self): 
        """serializes __objects to the JSON file (path: __file_path)"""
        newjson = json.dumps(self.__objects)
        print(newjson)
        #pass

    def reload(self): 
        """deserializes the JSON file to __objects"""
        pass

