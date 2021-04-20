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
        q = sys.argv[1]
    else:
        q = ''
    data = {'q': q}
    if requests.post(url, data=data).text == '{}\n':
        print('No result')
    else:
        try:
            data = requests.post(url, data=data).json
            print("[{}] {}".format(data['id'], data['name']))
        except:
            print("Not a valid JSON")
