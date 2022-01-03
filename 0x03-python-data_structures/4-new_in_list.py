#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    le = len(my_list)
    if idx < 0:
        my_list.copy()
    if idx >= le:
        my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return(new_list)
