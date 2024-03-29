#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
class Rectangle

Define Rectangle class module
"""
class Rectangle:
    """Define a Rectangle"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

