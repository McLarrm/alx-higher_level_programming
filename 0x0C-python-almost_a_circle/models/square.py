#!/usr/bin/python3
""" Defines the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new instance of the Square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
    """ Returns the dictionary representation of the square """
    return {
        'id': self.id,
        'size': self.width,
        'x': self.x,
        'y': self.y
    }
