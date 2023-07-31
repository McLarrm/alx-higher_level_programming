#!/usr/bin/python3
""" Function that adds two integer values """

def add_integer(a: int, b: int = 98) -> int:
    """Adds two numbers as integers, with a default value of 98 for the second number"""
    assert isinstance(a, (int, float)), "a must be an integer or a float"
    assert isinstance(b, (int, float)), "b must be an integer or a float"
    return int(a) + int(b)
