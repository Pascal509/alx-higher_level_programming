#!/usr/bin/python3
"""
is_kind_of_class function module

Define class
"""

def is_kind_of_class(obj, a_class):
    """
    Return True if obj inherits from a_class

    args:
    obj - an object
    a_class - a class
    """
    return(isinstance(obj,a_class))
