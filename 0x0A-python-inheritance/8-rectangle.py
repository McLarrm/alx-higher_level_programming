#!/usr/bin/python3
""" A class rectangle """


class BaseGeometry:
    """
    Base class representing geometry.
    """

    def area(self):
        """
        Computes the area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
