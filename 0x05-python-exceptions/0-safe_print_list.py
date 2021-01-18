#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        l_nbr = list(map(str, my_list[:x]))
        for nbr in l_nbr:
            print("{}".format(nbr), end="")
            count += 1
        print()
        return count
    except:
        return count
