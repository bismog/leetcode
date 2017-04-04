#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.dabeaz.com/coroutines/follow.py
import time

def follow(thefile):
    # According to pydoc file.seek, here whence==2 mean seek to end of file
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__":
    # For the sake of ignoring IOError before content of 'access-log' generated.
    while True:  
        try:
            logfile = open("access-log")
            for line in follow(logfile):
                print line,
        except IOError:
            pass
