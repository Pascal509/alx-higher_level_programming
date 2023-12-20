#!/usr/bin/python3
"""
class Sqaure
"""


class Square:
    """
    Initializes a square instance
    Attribute:
        size
    """
    def __init__(self, size=0):
        """
        initialize Square instance with __init__
        Attribute:
            __size__

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
