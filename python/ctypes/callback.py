#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ctypes

callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float, ctypes.c_float)

def greater_than(a, b):
    if a > b:
        return 1
    else:
        return 0

callback_func = callback_type(greater_than)

dll = ctypes.CDLL('./libfoo.so')
dll.foo(callback_func)


