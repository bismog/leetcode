#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.dabeaz.com/coroutines/countdown.py
def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1
    print "Done counting down."

if __name__ == "__main__":
    # for i in range(countdown(10)):
    for i in countdown(10):
        print i
