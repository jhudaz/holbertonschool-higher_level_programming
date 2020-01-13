#!/usr/bin/python3
# script that takes in a string and sends a search request to the Star Wars API
import requests
from sys import argv
# packages to handle the request


if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search={}".format(argv[1])
    r = requests.get(url).json()
    data = r['results']
    print("Number of results: {}".format(r["count"]))
    for person in data:
        print("{}".format(person['name']))
