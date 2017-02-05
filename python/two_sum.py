#!/usr/bin/env python
#-*- coding:utf-8 -*-

# arr = (2, 7, 11, 15)
arr = (2, 11, 15, 7)
target = 9

# def twosum():
#     # Find two number those sum equal to target(9)
#     try:
#         for x in arr:
#             complement = target - x
#             if complement in arr and arr.index(x) != arr.index(complement):
#                 return (x, complement)
#     except:
#         print "Exception raise"        
# 
# if __name__ == "__main__":
#     result = twosum()
#     print "x and y are: %d, %d" % result


##  http://stackoverflow.com/questions/30021060/two-sum-on-leetcode
def twosum(nums=(6, 7, 11, 15, 3, 6, 5, 3, 1), target=6):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    # print lookup
    # iters = ( (i+1, lookup.get(target-v)+1) for i, v in enumerate(nums) if lookup.get(target-v, i) != i)
    iters = ( (i+1, lookup.get(target-v)+1) for i, v in enumerate(nums) if lookup.get(target-v, i) > i)
    return iters
    # return next(iters , None)

if __name__ == "__main__":
    # print "x and y are: %d, %d" % twosum()
    for x, y in twosum():
        print "x and y are: %d, %d\n" % (x,y)

# def twosum():
#     """
#     >>> xxx=['a', 'b', 'c', 'd']
#     >>> xxxe=enumerate(xxx)
#     >>> dict(xxxe)
#     {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
#     >>> dict((v, i) for i,v in enumerate(xxx))
#     {'a': 0, 'c': 2, 'b': 1, 'd': 3}
#     """
    
