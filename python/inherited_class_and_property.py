#!/usr/bin/env python

class U(object):
    pass

class V(object):
    def __init__(self):
        self._abc = U()
    def kk(self):
        print "V:kk"

class W(V):
    @property
    def thisthat(self):
        print "W:tt"

w = W()

