#!/usr/bin/python3
import cmd
"""this module contain the cmd
commands:
-quit
-help
-create
-show
-destroy
-all
-update
"""

class HBNBCommand(cmd.Cmd):
	"""entry point for cmd"""
	prompt ='(hbnh) '	
	file = None
	
	def do_quit(Self, arg):
		"""quit cmd"""
		print("quit cmd")
	def do_create(self,arg):
		"""create new user"""
		print("new user created")
	

if __name__ == '__main__':
	HBNBCommand().cmdloop()
