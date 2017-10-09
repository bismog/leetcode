#!/usr/bin/env python

class U(object):
    def xx(self, rsc):
        print rsc

class V(U):
    def __init__(self):
        self.drv = U()
    @property
    def rsc(self):
        l = ['a','b','c',]
        return l
    def xx(self):
        self.drv.xx(self.rsc)

class W(V):
    @property
    def rsc(self):
        l = [1,3,9,]
        return l

v = V()
w = W()
w.xx()
