#!/usr/bin/python3
""" takes url and email and sends post request """
import requests
from requests.auth import HTTPBasicAuth
import sys

r = requests.get('https://api.github.com/users/{}'.format(sys.argv[1]),
                 auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
print(r.json().get('id'))
