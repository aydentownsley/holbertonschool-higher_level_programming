#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = 0
        if ord(i) >= 97 and ord(i) <= 122:
            num = 32
        print('{:c}'.format(ord(i) - num), end='')
    print()
