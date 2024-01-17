#!/usr\/bin/python3
from models.base import Base
"""
Define a subclass Rectangle that inherits from Base
"""
class Rectangle(Base):
    """Using class constructor initialise class atrributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """Get width of rectangle"""
        return self.__width

    def set_width(self, width):
        """Set width of rectangle and add validation logic"""
        self.__width = width 

    def get_height(self):
        """Get width of rectangle"""
        return self.__height

    def set_height(self,height):
        """Set width of rectangle and add validation logic"""
        self.__height = height

    def get_x(self):
        """Get width of rectangle"""
        return self.__x

    def set_x(self, x):
        """Set width of rectangle and add validation logic"""
        self.__x = x

    def get_y(self):
        """Get width of rectangle"""
        return self.__y

    def set_y(self, y):
        """Set width of rectangle and add validation logic"""
        self.__y = y
