#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from functools import wraps

class TraceCalls(object):
    """ Use as a decorator on functions that should be traced. Several
        functions can be decorated - they will all be indented according
        to their call depth.
    """
    def __init__(self, stream=sys.stdout, indent_step=2, show_ret=False):
        self.stream = stream
        self.indent_step = indent_step
        self.show_ret = show_ret

        # This is a class attribute since we want to share the indentation
        # level between different traced functions, in case they call
        # each other.
        TraceCalls.cur_indent = 0

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # import pdb;pdb.set_trace()
            indent = ' ' * TraceCalls.cur_indent
            argstr = ', '.join(
                [repr(a) for a in args] +
                ["%s=%s" % (a, repr(b)) for a, b in kwargs.items()])
            self.stream.write('%s%s(%s)\n' % (indent, fn.__name__, argstr))

            TraceCalls.cur_indent += self.indent_step
            ret = fn(*args, **kwargs)
            TraceCalls.cur_indent -= self.indent_step

            if self.show_ret:
                self.stream.write('%s--> %s\n' % (indent, ret))
            return ret
        return wrapper


# @TraceCalls()
# def iseven(n):
#     return True if n == 0 else isodd(n - 1)
# 
# @TraceCalls()
# def isodd(n):
#     return False if n == 0 else iseven(n - 1)
# 
# print(iseven(7))


#########
# Example
#########
# @TraceCalls()
# def foldr(func, init, seq):
#     if not seq:
#         return init
#     else:
#         return func(seq[0], foldr(func, init, seq[1:]))
# 
# @TraceCalls()
# def product_reducer(seqval, acc):
#     return seqval * acc
# 
# @TraceCalls()
# def product_with_foldr(seq):
#     return foldr(product_reducer, 1, seq)
# 
# product_with_foldr([2, 4, 6, 8])




#########
# Example
#########

@TraceCalls()
def foldl(func, init, seq):
    if not seq:
        return init
    else:
        return foldl(func, func(init, seq[0]), seq[1:])

@TraceCalls()
def digits2num_with_foldl(seq):
    return foldl(lambda acc, seqval: acc * 10 + seqval, 0, seq)

digits2num_with_foldl([2,3,4,5])
