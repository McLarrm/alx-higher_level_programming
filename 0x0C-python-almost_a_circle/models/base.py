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
            instance = cls(1)
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
