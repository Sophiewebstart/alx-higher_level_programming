#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, items in enumerate(my_list):
        if items == search:
            new_list[idx] = replace
    return new_list
