#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.dabeaz.com/coroutines/coroutine.py
# We'd better compare this example with that of grep.py

def coroutine(func):
    def start(*argc, **kargs):
        cr = func(*argc, **kargs)
        cr.next()
        return cr
    return start

if __name__ == "__main__":
    @coroutine
    def grep(pattern):
        print "Looking for %s" % pattern
        while True:
            line = (yield)
            if pattern in line:
                print line, 

    g = grep('python')
    # g.next()
    g.send('Yeah, but no, but yeah, but no')
    g.send('A series of tubes')
    g.send('python generators rock!')
