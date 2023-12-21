#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print result
    """

    try:
        result = a / b
    except ZeroDivisionError:
        return None  # Handle division by zero
    except (ValueError, TypeError):
        return None  # Handle cases where a or b are not valid integers
    else:
        print("Inside result: {:.1f}".format(result))
        return result
    finally:
        print("Inside finally block.")
