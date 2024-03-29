#!/usr/bin/python3
"""Import urllib modules"""
import urllib.parse
import urllib.request
import sys

"""Define main function"""
if __name__ == "__main__":
    """
    Write a Python script that takes in a URL, sends a request to the
    URL and displays the body of the response (decoded in utf-8).
    """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
