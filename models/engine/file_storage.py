#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        classes (dict): all classes names available.
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self, cls=None):
        """Return the dictionary __objects."""
        ret = {}
        if cls is None:
            return FileStorage.__objects
        name = cls.__name__
        for k, v in FileStorage.__objects.items():
            if name == k.split('.')[0]:
                ret[k] = v
        return ret

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    self.new(globals()[o["__class__"]](**o))
        except FileNotFoundError:
            pass

    def delete(self, name, id):
        """delete an object from the objects dictionary"""
        del self.__objects["{}.{}".format(name, id)]

    def delete(self, obj=None):
        """delete an object from obj dictionary"""
        if obj is None:
            return
        if "{}.{}".format(obj.__class__.__name__, obj.id) in FileStorage.__objects.keys():
            del FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]
