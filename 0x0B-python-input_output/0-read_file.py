#!/usr/bin/python3
"""
read_file function reads a text file and prints it to stdout
"""

def read_file(filename=""):
    """read specified file my_file_0.txt file"""
    with open(filename, encoding="utf-8") as myFile:
        """access and file using read_data"""
        read_file = myFile.read()
        print(read_file)
