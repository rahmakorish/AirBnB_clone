#!/usr/bin/python3
"""this module contain the cmd
commands:
-quit-help-create-show-destroy
-all-update"""
import sys
import cmd
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """entry point for cmd"""
    prompt = '(hbnh) '
    cls = ["BaseModel", "User", "City", "State", "Place", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, line):
        """create new user"""
        if not line:
            print("** class name missing **")
        elif line not in self.cls:
            print("** class doesn't exist **")
        else:
            print(f"{line}")

    def do_show(self, line):
        """prints string repr of instance"""
        try:
            clas, clas_id = line.split()
            if not line:
                print("** class name missing **")
            elif clas not in self.cls:
                print("** class doesn't exist **")
            else:
                print(f"{clas}")
        except ValueError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class"""
        try:
            clas, clas_id = line.split()
            if not line:
                print("** class name missing **")
            elif clas not in self.cls:
                print("** class doesn't exist **")
            else:
                print(f"{clas}")
        except ValueError:
            print("** instance id missing **")

    def do_all(self, line):
        if line not in self.cls:
            print("** class doesn't exist **")
        print(f"{line}")

    def do_update(self, line):
        """updates an instance"""
        try:
            clas, clas_id, clas_attr, attr_value = line.split()
            if not line:
                print("** class name missing **")
            elif clas not in self.cls:
                print("** class doesn't exist **")
            else:
                print(f"{clas}")
        except ValueError:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
