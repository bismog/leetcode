#!/usr/bin/env python

class XXX(object):
    def __init__(self):
        self.a = 5

    def __call__(self, k=8):
        self.a = k

x = XXX()
print x.a
#x()
x.__call__()
print x.a

