#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        n = my_list[0]
        for nbr in my_list:
            if n < nbr:
                n = nbr
        return n
    else:
        return None
