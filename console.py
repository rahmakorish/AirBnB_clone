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

    def do_quit(Self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """create new user"""
        print("new user created")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
