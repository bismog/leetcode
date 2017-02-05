#!/usr/bin/env python
# -*- coding:utf-8 -*-

nums = [1, 2, 3, 4, 3, 2, 1]

def exclusive_or(x, y):
    return x^y

out = reduce(exclusive_or, nums)
print "The single number is ", out
