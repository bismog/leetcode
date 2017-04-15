#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

exit_flag = 0

class myThread(threading.Thread):
    def __init__(self, id, name, counter):
        # super(self, myThread).__init__()
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.counter = counter

    def run(self):
        print 'starting' + self.name
        print_time(self.name, self.counter, 5)
        print 'exiting' + self.name

def print_time(name, delay, counter):
    while counter:
        # if exit_flag:
        #     name.exit()
        time.sleep(delay)
        print '%s: %s' % (name, time.ctime(time.time()))
        counter -= 1

thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

thread1.start()
thread2.start()

print 'Exiting Main Thread'

