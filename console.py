#!/usr/bin/python3
"""this module contain the cmd
commands:
-quit-help-create
-show-destroy
-all-update
"""
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point for cmd"""
    prompt = '(hbnh) '
    """file = None"""

    def do_quit(Self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """end of line command"""
        print('\n')
        return True

    def help_quit(self):
        """help quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """EOF"""
        print("End Of Line\n")

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """create new user"""
        print("new user created")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
