#!/usr/bin/python3
"""
class square defines square
"""


class Square:
    """
    class square defines square
    Attributes:
        size
    """
    def __init__(self, size=0):
        """
        initializes square sequence
        Attributes:
            size
        """
        self.size = size

    @property
    def size(self):
        """
        Getter retrieves size of square an returns size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting size of square, TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and return "int" area of square
        """
        return self.__size ** 2
