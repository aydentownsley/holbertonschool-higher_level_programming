#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print('{:c}'.format(ord(i) - 32), end='')
        if ord(i) >= 65 and ord(i) <= 90:
            print('{:c}'.format(ord(i)), end='')
    print()
