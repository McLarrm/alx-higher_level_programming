#!/usr/bin/python3
""" Defines the Base class """
import json


class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new instance of the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of dictionaries represented by a JSON string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance from a dictionary """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1, 0, 0)  # Modify this line to set the correct x and y values
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Loads a list of instances from a JSON file """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON representation of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of instances to a JSON file """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_str)
