#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints integer with value and returns a boolean
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
