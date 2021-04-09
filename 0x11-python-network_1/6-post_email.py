#!/usr/bin/python3
""" takes url and email and sends post request """
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
