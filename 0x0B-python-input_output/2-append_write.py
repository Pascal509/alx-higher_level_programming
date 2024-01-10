#!/usr/bin/python3
"""
append_write: appends a string at the end of a text file

Args:
    filename - file_append.txt file
    text - Text to be appended
"""
def append_write(filename="", text=""):
    """append string to file"""
    with open(filename, 'a', encoding="UTF-8") as a:
        """access appended file"""
        append_file = a.write(text)
        return append_file
