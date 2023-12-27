#!/usr/bin/python3
"""
Defines class Square of a square
"""



class Square:
    """
    Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance in size (int) and position(tuple)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method retrieves the size of square returning an int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting size of square with TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter retrieves position of square and returns tuple
        """
        return self.__postion

    @position>setter
    def position(self, value):
        """
        Setter method sets position of the square with TypeError and ValueError
        """
         if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
             raise TypeError("position must be a tuple of 2 positive integers")
         self.__position = value

    def area(self):
        """
        Calculates area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #
        """
         if self.__size == 0:
             print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

