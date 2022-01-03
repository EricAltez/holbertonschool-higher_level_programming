#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    if idx < 0:
        return None
    if idx >= le:
        return None
    else:
        return my_list[idx]
