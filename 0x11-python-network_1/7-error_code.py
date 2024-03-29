#!/usr/bin/python3
"""Import modules"""
import requests
import sys

"""Define main module"""


if __name__ == "__main__":
    """
    Write a Python script that takes in a URL, sends a request to the
    URL and displays the body of the response.
    """
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        print(req.text)
    elif req.status_code >= 400:
        print('Error code: ', req.status_code)
