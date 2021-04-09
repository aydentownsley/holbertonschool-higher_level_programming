#!/usr/bin/python3
""" takes url and email and sends post request """

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    r = requests.get('https://api.github.com/users/',
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    try:
        out = r.json()
        print(out['id'])
    except:
        print("None")
