#!/usr/bin/python3
# script that takes in a letter and sends a POST request to /search_user
import requests
from sys import argv
# packages to handle the request


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    try:
        r = requests.post(url, data={'q': q}).json()

        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
