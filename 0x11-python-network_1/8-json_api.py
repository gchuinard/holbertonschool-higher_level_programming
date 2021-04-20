#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        value = {'q': sys.argv[1]}
    else:
        value = {'q': ""}
    if requests.post(url, data=value).text == '{}\n':
        print('No result')
    else:
        try:
            data = requests.post(url, data=value).json()
            print("[{}] {}".format(data['id'], data['name']))
        except ValueError:
            print("Not a valid JSON")
