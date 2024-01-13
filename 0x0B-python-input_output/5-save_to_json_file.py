#!/usr/bin/python3
import json
"""
From save_to_json_file function module

Define save_to_json_file
"""
def save_to_json_file(my_obj, filename):
    """
    write and object to a text file with JSON

    Args:
    my_obj - 
    filename -
    """
    with open(filename, 'w', encoding="utf-8") as w:
        write_obj = json.dump(my_obj, w)
        return write_obj
