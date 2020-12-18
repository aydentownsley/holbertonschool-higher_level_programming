#!/usr/bin/python3
def weight_average(my_list=[]):
    mul_sum = 0
    denom = 0
    a = [el[0] * el[1] for el in my_list]
    b = [el[1] for el in my_list]
    for i in range(len(a)):
        mul_sum += a[i]
    for j in range(len(b)):
        denom += b[j]
    print(a)
    print(b)
    print(mul_sum)
    print(denom)
    return mul_sum / denom
