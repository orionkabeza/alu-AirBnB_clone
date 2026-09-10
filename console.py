#!/usr/bin/python3
"""Defines the HBNB command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print its id.

        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances.

        Usage: all [class name]
        """
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        result = []
        for key, obj in storage.all().items():
            if len(args) == 0 or key.split(".")[0] == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or updating an attribute.

        Usage: update <class name> <id> <attribute name> "<value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = all_objects[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
