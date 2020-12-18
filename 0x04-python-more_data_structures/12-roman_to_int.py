#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    res = 0
    nmrls = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    newarr = [nmrls[i] for i in roman_string]
    for j in range(len(newarr)):
        if j != len(newarr) - 1:
            if newarr[j] < newarr[j + 1]:
                res = res - newarr[j]
            else:
                res = res + newarr[j]
        else:
            res = res + newarr[j]
    return res
