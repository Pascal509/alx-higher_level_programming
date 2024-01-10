#!/usr/bin/python3
"""
Parent class: is_same_class returns True for specified dataype

Define is_same_class function.
"""



def is_same_class(obj, a_class):
    """
    Module returns an instance of a_class

    Args:
    obj is an object.
    a_class is a class
    """
    return (type(obj) is a_class)
