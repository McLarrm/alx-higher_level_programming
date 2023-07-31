#!/usr/bin/python3
""" Function that adds two integer values"""


def add_integer(a: int, b: int = 98) -> int:
    """Adds two numbers as integers, with a default value of 98 for the second number"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
