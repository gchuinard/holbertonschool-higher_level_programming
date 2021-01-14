#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    i = 0
    for nbr in my_list:
        if my_list[i] % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
        i += 1
    return list_result
