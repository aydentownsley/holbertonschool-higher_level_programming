#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dict = dict(a_dictionary)
    for i in b_dict:
        if b_dict[i] == value:
            del a_dictionary[i]
    return a_dictionary
