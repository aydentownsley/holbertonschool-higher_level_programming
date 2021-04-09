#!/usr/bin/python3
""" takes url and email and sends post request """
import urllib.request
import urllib.parse
import sys

a = {'email': sys.argv[2]}
email = urllib.parse.urlencode(a).encode('utf-8')
request = urllib.request.Request(sys.argv[1], email)
with urllib.request.urlopen(request) as r:
    print(r.read().decode('utf-8'))
