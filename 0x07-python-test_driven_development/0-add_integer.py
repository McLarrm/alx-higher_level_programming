#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(5, 3)
        8
        >>> add_integer(5.5, 3.2)
        8
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
