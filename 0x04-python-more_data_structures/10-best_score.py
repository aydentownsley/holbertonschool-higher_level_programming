#!/usr/bin/python3
#
# best_score - finds biggerst key value (int)
#
# @a_dictionary: dict
#
# Return: biggest key value


def best_score(a_dictionary):
    poss_max = 0
    best_max = ''
    if a_dictionary is None or a_dictionary == {}:
        return None
    for key in a_dictionary.keys():
        if a_dictionary[key] > poss_max:
            poss_max = a_dictionary[key]
            best_max = key
    return best_max
