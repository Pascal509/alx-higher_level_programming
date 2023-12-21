#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_data = 0

    try:
        for i in range(x):
            print(my_list[i], end=" ")
            print_data += 1
    except IndexError:
        pass

    print()
    return print_data
