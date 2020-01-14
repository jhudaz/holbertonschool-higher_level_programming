#!/usr/bin/python3
# script  using github api
import requests
from sys import argv
# package to handle the request


if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, passw)).json()
    if 'id' in r:
        print(r['id'])
    else:
        print('None')
