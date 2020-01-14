#!/usr/bin/python3
# get the 10 last commits from a repository
import requests
from sys import argv
# packages to handle the request


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    print(url)
    commits = requests.get(url).json()

    for data in commits:
        print("{}: {}".format(data['sha'], data['author']['login']))
