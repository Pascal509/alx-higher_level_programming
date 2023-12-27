#!/usr/bin/python3
"""
Defines class Square of a square
Attributes:
    size
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        Initializes square instance
        Attributes:
            size
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method retrieves size of square
        Attributes:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size of square, TypeError and ValueError
        Attributes:
            value, size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Attributes:
            Area
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints square using # and empty line
        Atrributes:
            my_print
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

