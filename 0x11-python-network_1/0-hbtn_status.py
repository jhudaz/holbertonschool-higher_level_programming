#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status
from urllib.request import urlopen
# package to handle request


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode()))
