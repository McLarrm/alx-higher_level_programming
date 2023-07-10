#!/usr/bin/python3
""" Inherits from a Class """


def inherits_from(obj, a_class):
    """ Checks if the object is an instance of a class that inherited """
    return (isinstance(obj, a_class) and type(obj) != a_class)
