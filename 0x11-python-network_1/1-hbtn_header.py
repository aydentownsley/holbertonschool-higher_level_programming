#!/usr/bin/python3
""" sends request and display value of X-Request-Id """

if __name__ == "__main__":
    import urllib.request
    import sys

    arg = sys.argv
    site = urllib.request.Request(arg[1])

    with urllib.request.urlopen(site) as r:
        print(r.headers.get('X-Request-Id'))
