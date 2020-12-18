#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul_sum = 0
    denom = 0
    a = [el[0] * el[1] for el in my_list]
    b = [el[1] for el in my_list]
    for i in range(len(a)):
        mul_sum += a[i]
    for j in range(len(b)):
        denom += b[j]
    return mul_sum / denom
