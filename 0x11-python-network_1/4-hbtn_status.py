#!/usr/bin/python3
"""
Import modules
"""
import requests

if __name__ == "__main__":
    """
    Write a Python script that fetches https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
