#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status using request package
import requests
# package to handle a request


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
