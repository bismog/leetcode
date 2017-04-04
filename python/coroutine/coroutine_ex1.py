#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Scheduler(object):

    def __init__(self):
        self.queue = []
        self.task_num = 0

    def new(self, task):
        self.queue.append(task)
        self.task_num += 1

    def loop(self):
        while self.task_num:
            task = self.queue.pop(0)
            #self.task_num -= 1
            ppp = task.next()
            print ppp
            ppp = task.next()
            print ppp
            ppp = task.next()
            print ppp
            self.queue.append(task)

def task1():
    c1 = 0
    while True:
        # Do something
        yield "This is task1", c1
        # yield c1
        c1 += 1

def task2():
    c2 = 0
    while True:
        # Do something
        yield "This is task2", c2
        # yield c2
        c2 += 1

scheduler = Scheduler()
scheduler.new(task1())
scheduler.new(task2())
scheduler.loop()

