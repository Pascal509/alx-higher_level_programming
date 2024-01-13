#!/usr/bin/python3
import json
"""
class_to_json function module

Define function class_to_json
"""

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure for JSON serialization of an object
    """
    return obj.__dict__

