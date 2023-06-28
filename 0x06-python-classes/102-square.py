#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize Square instance with size"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.size ** 2

    def __eq__(self, other):
        """Check if two squares have equal areas"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if two squares have different areas"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """Check if the area of the first square is greater than the second"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Check if the area of the first square is greater than or equal to the second"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Check if the area of the first square is less than the second"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Check if the area of the first square is less than or equal to the second"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
