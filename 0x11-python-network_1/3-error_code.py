#!/usr/bin/python3
import urllib.parse
import urllib.request
import urllib.error
from sys import argv
# package to handle the requests and take the arguments from the user input


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print("{}".format(data.decode()))

    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
