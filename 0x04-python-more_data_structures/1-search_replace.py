#!/usr/bin/python3
#
# search_replace - search list for element
# and replace all occurences in a new list
#
# @my_list: list to search
# @search: element to search for
# @replace: element to replace with
#
# Return: new list
def search_replace(my_list, search, replace):
    rep_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            rep_list.append(replace)
        else:
            rep_list.append(my_list[i])
    return rep_list
