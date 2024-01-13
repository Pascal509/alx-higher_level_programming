#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
Write scripts that adds all arguments to a Python list and saves them as a filw

Args:
    args

"""
def add_arguments(args):

    try:
        current_list = load_from_json_file("add_item.json")
    except:
        current_list = []

    current_list.extend(args)

    save_to_json_file(current_list, "add_item.json")

if __name__ == "__main__":
    args = sys.argv[1:]

    add_arguments(args)
