#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.dabeaz.com/coroutines/pipeline.py
from follow import follow

def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            print line

if __name__ == "__main__":
    logfile = open("access-log")
    loglines = follow(logfile)
    pylines = grep('python', loglines)

    for line in pylines:
        print line
