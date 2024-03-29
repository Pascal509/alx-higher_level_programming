#!/usr/bin/python3
"""Import modules"""
import requests
import sys

if __name__ == "__main__":
    """
    Write a Python script that takes in a URL, sends a request to the
    URL and displays the value of the variable X-Request-Id in the
    response header
    """
    url = sys.argv[1]
    body = requests.get(url)
    req = body.headers['X-Request-Id']
    print(req)
