#!/usr/bin/python3
"""
Module writes a string to text file and returns number of Characters

Args:
    filename(str): text
"""

def write_file(filename="", text=""):
    """parse in the file to write/overwrite"""
    with open(filename, 'w', encoding="utf-8") as f:
        """write into the file"""
        write_file = f.write(text)
        """Return the written file"""
        return write_file
