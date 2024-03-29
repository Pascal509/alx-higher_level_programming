#!/usr/bin/python3
"""Import module"""
import requests
import sys

"""Define main function"""


if __name__ == "__main__":
    """
    Write a Python script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the letter as
    a parameter.
    """
    url = 'http://0.0.0.0:5000/search_user'

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    q = {'q': q}
    body = requests.post(url, data=q)
    try:
        obj = r.json()
        if not obj:
            print('No result')
        else:
            print(f'[{obj["id"]}] {obj["name"]}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
