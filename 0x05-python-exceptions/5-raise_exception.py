#!/usr/bin/python3
def raise_exception():
    """
    Raises an exception.
    """
    try:
        raise TypeError("This is a type exception.")
    except TypeError as e:
        print(f"Caught an exception: {e}")
    finally:
        print("Finally block executed.")
