#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
from urllib import parse, request
import sys


if __name__ == "__main__":
        value = {'email': sys.argv[2]}
        data = parse.urlencode(value)
        data = data.encode('ascii')

        with request.urlopen(request.Request(sys.argv[1], data)) as res:
            print(res.read().decode('utf-8'))
