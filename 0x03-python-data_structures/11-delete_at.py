#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        idx += 1
        my_list.remove(idx)
    return my_list
