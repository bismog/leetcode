#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://realpython.com/blog/python/primer-on-python-decorators/

from decorator07 import my_decorator

@my_decorator
def just_some_function():
    print('Wheee!')

just_some_function()
