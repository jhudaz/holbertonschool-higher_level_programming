#!/usr/bin/python3
# script that takes in a letter and sends a POST request to /search_user
import requests
from sys import argv
# packages to handle the request


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        r.json()

        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    exception:
        print("Not a valid JSON")
