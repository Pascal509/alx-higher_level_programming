#1/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(d, a_dictionary[d])) for d in sorted(a_dictionary)]
