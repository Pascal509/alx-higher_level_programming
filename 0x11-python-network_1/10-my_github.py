#!/usr/bin/python3
"""Import module"""
import requests
import sys

"""Define main module"""


if __name__ == "__main__":
    """
    Write a Python script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id
    """
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    res = requests.get(url, auth=(username, password))
    if res.status_code == 200:
        user_info = res.json()
        user_id = user_info['id']
        print(user_id)
    else:
        print(f"failed to retrieve user information: {response.status_code}")
