#!/usr/bin/env python

def sum_pairs(ints, s):
    i_hub = []
    for i,v in enumerate(ints):
        if s-v not in ints[i+1:]:
            continue
        i_diff = ints.index(s-v, i+1)
        i_hub.append([i, i_diff])

    if not i_hub:
        return None

    i_last = [max(ele) for ele in i_hub]
    mini_last = min(i_last)
    b = ints[mini_last]
    a = s - b
    return [a, b]

# ints = [10, 5, 2, 3, 7, 5]
ints = [5, 9, 13, -3]
print sum_pairs(ints, 10)
