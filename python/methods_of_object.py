#!/usr/bin/env python
#-*- coding:utf-8 -*-

def methods_of(obj):
    """Get all callable methods of an object that don't start with underscore

    returns a list of tuples of the form (method_name, method)
    """
    result = []
    for i in dir(obj):
        if callable(getattr(obj, i)) and not i.startswith('_'):
            result.append((i, getattr(obj, i)))
    return result


class UUU(object):
    def __init__(self):
        pass

    def abc(self):
        pass

    def kkk(self):
        pass

    def xyz(self):
        pass


uuu = UUU()
for action, action_fn in methods_of(uuu):
    print action, action_fn
