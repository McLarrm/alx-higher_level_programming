#!/usr/bin/python3
""" Defines the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a new instance of the Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Width, Getter, Setter """
    @property
    def width(self):
        """ Getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ X Getter, Setter """
    @property
    def x(self):
        """ Getter for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Public Method """
    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle using the '#' character """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Updates the attributes of the rectangle based on the arguments """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a new instance with attributes already set """
        instance = cls(1, 1)  # Create a dummy instance with default values
        instance.update(**dictionary)
        return instance
