#!/usr/bin/python3
"""
Define class BaseGeometry

"""
class BaseGeometry:
    """
    Public instance method: def area
    """
    def area(self):
        """raise an Exception"""
        raise Excetion("area() is not implemented")

    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
