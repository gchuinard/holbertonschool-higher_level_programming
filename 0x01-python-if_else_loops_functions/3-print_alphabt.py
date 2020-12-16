#!/usr/bin/python3
for c in range(26):
    if (c != 4 and c != 16):
        print("{:c}".format(c + 97), end="")
