#!/usr/bin/python3
""" takes url and email and sends post request """

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        output = r.json()
        if output:
            print("[{}] {}".format(output['id'], output['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
