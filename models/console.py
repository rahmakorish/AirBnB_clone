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
		"""Quit command to exit the program"""
		return True
	def do_EOF(self, arg):
		"""end of line command"""
		print('\n')
		return True
	def do_create(self,arg):
		"""create new user"""
		print("new user created")
	

if __name__ == '__main__':
	HBNBCommand().cmdloop()
