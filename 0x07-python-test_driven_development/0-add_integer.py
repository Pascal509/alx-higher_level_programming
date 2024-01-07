#!/usr/bin/python3
"""
Docstring defines a module for the functions

Return: an integer
"""

def add_integer(a, b=98):
    """
    Args:
    a is an integer
    b is an integer

    Return:

    Raises:
    TypeError: raised with an error

    """
    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance (b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    sum = a + b

    return sum
