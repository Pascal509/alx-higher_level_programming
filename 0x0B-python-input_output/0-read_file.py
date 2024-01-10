#!/usr/bin/python3
"""
read_file function reads a text file and prints it to stdout
"""

def read_file(filename=""):
    """read specified file my_file_0.txt file"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data)
