#!/usr/bin/python3
def magic_calculation(elephant, bongo):
    sqwuack = 0
    for rant in range(1, 3):
        try:
            if rant > elephant:
                raise Exception('Too Far')

            sqwuack = sqwuack + (elephant ** bongo) / rant
        except:
            sqwuack = elephant + bongo
            break
    return sqwuack
