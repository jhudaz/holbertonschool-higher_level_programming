#!/usr/bin/python3
# sends a POST request to the passed URL with the email as a parameter
import requests
from sys import argv
# packages to handle request


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    values = {'email': email}

    r = requests.post(url, data=values)

    print("{}".format(r.text))
