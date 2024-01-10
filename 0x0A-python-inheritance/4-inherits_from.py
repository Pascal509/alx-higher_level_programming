#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    module: inherits_from returns an object of an instance of a class directly or indirectly

    Args:
    obj - object of a_class
    a_class - class inherited
    """
    return(issubclass(type(obj), a_class) and not (type(obj) is a_class))
