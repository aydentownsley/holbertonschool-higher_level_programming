#!/usr/bin/python3
""" takes url and email and sends post request """
import requests
import sys

r = requests.get(sys.argv[1])
if r:
    print(r.content.decode('utf-8'))
elif r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
