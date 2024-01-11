#!/usr/bin/python3
import json
"""
from_json_string: Function returns an object Python data structure

Args: my_str_

"""
def from_json_string(my_str):
    """return object with JSON string"""
    return json.loads(my_str)
