#!/usr/bin/env python
#-*- coding:utf-8 -*-

def count():
    yield 1
    yield 2
    yield 3

a = count()
print a.next()
print a.next()
print a.next()
print a.next()


