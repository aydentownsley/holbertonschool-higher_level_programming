#!/usr/bin/python3
""" takes url and email and sends post request """

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id', None))
