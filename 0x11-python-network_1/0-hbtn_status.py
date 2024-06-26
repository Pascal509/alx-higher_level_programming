#!/usr/bin/python3
"""import modules"""
import urllib.request


"""Define main function"""


def main():
    """
    Write a Python script that fetches https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        utf8_content = html.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", utf8_content)


if __name__ == "__main__":
    main()
