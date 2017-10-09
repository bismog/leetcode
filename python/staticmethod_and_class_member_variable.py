#!/usr/bin/env python

class XXX(object):
    def __init__(self):
        self.abc = 345
        self.xyz = "789"

    @staticmethod
    def xxx():
        print self.abc
        print self.xyz


XXX.xxx()
