#!/usr/bin/python3
""" takes url and email and sends post request """
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
