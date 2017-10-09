#!/usr/bin/env python
#encoding=UTF-8


import threading
import time

def hello(name):
    print "hello %s" % name

    #set timer for next
    global timer
    timer = threading.Timer(2.0, hello, ["hawk"])
    timer.start()

if __name__ == "__main__":
    global timer
    timer = threading.Timer(2.0, hello, ["hawk"])
    timer.start()
