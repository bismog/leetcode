#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently/

def my_coroutine():
    while True:
        received = (yield)
        print('Received:', received)

it = my_coroutine()
# next(it)
it.next()
it.send('First')
it.send('Second')
