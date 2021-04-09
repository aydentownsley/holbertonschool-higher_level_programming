#!/usr/bin/python3
""" fetch https://intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        site = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(site)))
        print("\t- content: {}".format(site))
        print("\t- utf8 content: {}".format(site.decode('utf-8')))
