#!/usr/bin/bash
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialise rectangle instance with width and height"""
        self._Rectangle__height = 0
        self._Rectangle__width = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method used to retrieve width"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Setter to set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        """Getter method used to retrieve height"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """Setter to set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__height = value
