#!/usr/bin/env python

class XXX(object):
    def __init__(self, p1, p2=None, p3=None, p4=None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

xxx = XXX(p2='222', p3='111', p4='444')
print xxx.p1, xxx.p2, xxx.p3, xxx.p4
