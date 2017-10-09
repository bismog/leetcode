#!/usr/bin/env python

def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list

xxx = bad_append('one')
print xxx
xxx = bad_append('two')
print xxx
xxx = bad_append('three')
print xxx


def good_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list

print good_append('one')
print good_append('two')
print good_append('three')
