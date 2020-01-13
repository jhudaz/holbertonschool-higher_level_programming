#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status
from urllib.request import urlopen
# package to handle request


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode()))
