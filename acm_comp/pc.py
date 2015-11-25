#!/usr/bin/python
import copy

the_in = raw_input().strip().split()

method = the_in[1]
size = int(the_in[0])

def split_list(l):
    return l[len(l)/2:], l[:len(l)/2]

def merge(r, l, m):
    z = []
    if m == "in":
        return [item for pair in zip(r, l) for item in pair]
    elif m == "out":
        return [item for pair in zip(l, r) for item in pair]

if __name__ == "__main__":
    orig_list = range(size)
    left, right = split_list(orig_list)
    temp_list = merge(left, right, method)
    i = 1
    while temp_list != orig_list:
        left, right = split_list(temp_list)
        temp_list = merge(left, right, method)
        i += 1
    print i
