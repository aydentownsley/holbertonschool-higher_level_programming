#!/usr/bin/python3
#
# multiple_returns - return tuple with length of string
# and first character of string
#
# @sentence: string
#
# Return: length and first char
# OR 0 and None
# OR None if no string


def multiple_returns(sentence):
    if not sentence:
        return 0, None
    if len(sentence) == 0:
        a = 0
        b = None
    else:
        a = len(sentence)
        b = sentence[0]

    return a, b
