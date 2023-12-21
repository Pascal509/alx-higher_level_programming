#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raise name exception with custom message
    """

    try:
        raise NameError(message)
    except NameError as ne:
        print (f"Exception found")
    finally:
        print("Finally block executed")
