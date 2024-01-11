#!/usr/bin/python3
import json

"""
to_json_string: function returns JSON representation of an object

Args:
    my_obj - 
"""
def to_json_string(my_obj):
    rep_json = json.dumps(my_obj)
    return rep_json
