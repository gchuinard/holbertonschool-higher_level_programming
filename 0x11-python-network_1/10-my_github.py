#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(username, password)).json()
    print(req.get('id'))
