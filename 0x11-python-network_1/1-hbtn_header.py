#!/usr/bin/python3
# sends a request to the URL and displays the value of the X-Request-Id
from urllib.request import urlopen
from sys import argv
# package to handle request and get the arguments from the user


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        headers = response.info()
        if 'X-Request-Id' in headers:
            print(headers['X-Request-Id'])
