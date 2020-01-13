#!/usr/bin/python3
# sends a request to the URL and displays the body of the response.
import requests
from sys import argv
# packages to handle the request


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
