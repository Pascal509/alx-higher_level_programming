#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


"""
Define a subclass Rectangle that inherits from Base
"""
class Rectangle(Base):
    """Using class constructor initialise class atrributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """Get width of rectangle"""
        return self.__width

    def set_width(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    def get_height(self):
        """Get width of rectangle"""
        return self.__height

    def set_height(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    def get_x(self):
        """Get width of rectangle"""
        return self.__x

    def set_x(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value <= 0:
            raise ValueError("X must be >= 0")
        self.__x = value

    def get_y(self):
        """Get width of rectangle"""
        return self.__y

    def set_y(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value
