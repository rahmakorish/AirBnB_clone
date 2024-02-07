#!/usr/bin/python3
"""this module represent base class"""
import json 
import uuid
import datetime

mydict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}

my_json = json.dumps(mydict)

print (my_json)
