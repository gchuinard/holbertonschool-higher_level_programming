#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set1 = set(set_1.difference(set_2))
    new_set2 = set(set_2.difference(set_1))
    return new_set1.union(new_set2)
