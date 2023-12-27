#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints integers while handling potential exceptions
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return false