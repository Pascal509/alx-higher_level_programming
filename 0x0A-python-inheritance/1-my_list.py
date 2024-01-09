#!/usr/bin/python3
"""
Parent class MyList
"""
class MyList(list):
    """
    Public instance method which prints a sorted list
    """
    def print_sorted(self):
        print(sorted(self))
