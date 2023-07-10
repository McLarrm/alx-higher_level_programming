#!/usr/bin/python3
""" Attribute to an object """


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible
    """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
