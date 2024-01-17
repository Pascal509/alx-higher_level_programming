#!/usr/bin/python3
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

    @property
    def width(self):
        """Get width of rectangle"""
        return self__width

    @width.setter
    def width(self, new_width):
        """Set width of rectangle and add validation logic"""
        self.validate_integer("width", value, False)
        self.__width = value






