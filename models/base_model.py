#!/usr/bin/python3
"""this module represent base class"""


class BaseModel:
	"""class base model"""
	def __init__(self, *args, **kwargs):
	def __init__(self, id, created_at, updated_at, __str__):
		"""init function"""
		self.id=#uniqu id
		self.created_at=datetime.time().now()#time object created
		self.updated_at=datetime.time().now()#time object created or update
		self.__str__=#[<class name>] (<self.id>) <self.__dict__>
	
	def save(self):
	#update the update_At attribute
	def to_dict(self):
	#return dictionary of the instance
	
