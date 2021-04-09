#!/usr/bin/python3
""" takes url and email and sends post request """

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as r:
            out = r.read()
            print(out.decode('utf-8'))
    except HTTPError as err:
        print("Error code: ", err.code)
