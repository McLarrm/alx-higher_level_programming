#!/usr/bin/python3
""" Attribute to an object """


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible
    """
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    if not hasattr(obj.__class__, attr):
        setattr(obj.__class__, attr, property())

    setattr(obj, attr, value)
