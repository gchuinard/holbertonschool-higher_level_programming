#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_t = (0, None)
    if sentence:
        tuple_t = (len(sentence), sentence[0])
    return tuple_t
