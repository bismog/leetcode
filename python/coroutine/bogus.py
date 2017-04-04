#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.dabeaz.com/coroutines/bogus.py

def countdown(n):
    print 'Counting down from', n
    while n >= 0:
        newvalue = (yield n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

c = countdown(7)
for x in c:
    print x
    if x == 5:
        c.send(3)
