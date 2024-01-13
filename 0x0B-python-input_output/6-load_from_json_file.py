#!/usr/bin/python3
import json
"""
load_from_json_file from module

Define load_from_json_file
"""
def load_from_json_file(filename):
    """
    creates an object from JSON file

    Args:
        filename -
    """
    with open(filename, encoding="utf-8=") as myFile:
        """load from json file"""
        return json.loads(myFile.read())

