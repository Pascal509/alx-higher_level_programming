#!/usr/bin/python3

"""import modules"""
import urllib.request
import sys

"""Define main module"""
if __name__ == "__main__":

    """
    Write a Python script that takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id variable found in
    the header of the response.
    """
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        My_id = response.getheader('X-Request-Id')
        print(My_id)
