#!/usr/bin/python3
"""import modules"""
import requests
import sys

"""Define main module"""
if __name__ == "__main__":
    """
    The Holberton School staff evaluates candidates applying for a
    back-end position with multiple technical challenges, like this one
    """
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    res = requests.get(url)

    if res.status_code == 200:
        commits = res.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to fetch commits: {res.status_code}")
