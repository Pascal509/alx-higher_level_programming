#!/usr/bin/python3
def add_integer(a, b=98):

    #Check if a is not integer or a float
    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance (b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    sum = a + b

    return sum

import doctest
doctest.testfile("0-add_integer.txt")
