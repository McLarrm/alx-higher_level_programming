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
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            for argmts in range(len(args)):
                if argmts == 0:
                    self.id = args[argmts]
                if argmts == 1:
                    self.size = args[argmts]
                if argmts == 2:
                    self.x = args[argmts]
                if argmts == 3:
                    self.y = args[argmts]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the square """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
