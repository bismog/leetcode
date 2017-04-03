#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Count(object):

    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        self.count = self.count + 1
        return self.count

a = Count()
print a.next()
# print a.send(None)
print a.next()

b = a.__iter__()
print b.next()

c = Count()
print c.next()

