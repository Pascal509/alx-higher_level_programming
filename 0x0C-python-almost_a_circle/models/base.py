#!/usr/bin/python3
"""
Define class Base

"""
class Base:
    """assign the public instance attribute id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Check if id is None"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
