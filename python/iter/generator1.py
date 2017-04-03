#!/usr/bin/env python
#-*- coding:utf-8 -*-

def count():
    c = 0
    while True:
        c = c + 1
        yield c

a = count()
print a.next()
print a.send(None)
# print a.send()
print a.next()

b = a.__iter__()
print b.next()

c = count()
print c.next()


