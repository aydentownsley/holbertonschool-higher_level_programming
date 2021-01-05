#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    pnum = 0
    try:
        for idx in range(x):
            if type(my_list[idx]) is int:
                print(my_list[idx], end="")
                pnum += 1
            idx += 1
        print()
        return pnum
    except:
        raise
        print("IndexError: list index out of range")
        return pnum
