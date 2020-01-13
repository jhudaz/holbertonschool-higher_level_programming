#!/usr/bin/python3
# takes in a URL and an email, sends a POST request to the passed URL
import urllib.parse
import urllib.request
from sys import argv
# package to handle the requests and take the arguments from the user input


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        data = response.read()
        print("{}".format(data.decode()))
