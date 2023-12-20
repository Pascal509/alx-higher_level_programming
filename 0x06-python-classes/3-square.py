#!/usr/bin/python3
"""
private instance attribute
Attributes:
    __size__
"""


class Square:
    """
    Attributes:
        size
    """
    def __init__(self, size=0):
        """
        Initialize Square instance
        """
        if not isinstance(size, int):
            raise TypeError("size is an integer")
        elif size < 0:
            raise ValueError("size >= 0")
        else:
            self.__size = size

    def area(self):
            """
            Calculates and return 'int', the area of the square
            """
            return self.__size ** 2
