#!/usr/bin/python3
# script that takes in a URL, sends a request and displays X-Request-Id
import requests
from sys import argv
# packages to handle the requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    data = r.headers
    print("{}".format(data['x-request-id']))
