#!/usr/bin/python3
"""
takes 2 arguments in order to solve this challenge.
"""
import requests
import sys


if __name == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    json = requests.get(url).json()
    for i in range(len(json)):
        jsonFil = json[i]
        print("{}: {}".format(jsonFil.get("sha"),
                              jsonFil.get("commit").get("author").get("name")))
    if i == 9:
        break
