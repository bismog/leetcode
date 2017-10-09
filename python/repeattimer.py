#!/usr/bin/env python
#encoding=UTF-8


from threading import Event, Thread
import time

class repeat_timer(Thread):
    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def run(self):
        count = 0
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                count += 1

    def cancel(self):
        self.finished.set()

def hello(name):
    print "hello %s(current time:%s)" % (name, time.time())

if __name__ == "__main__":
    t = repeat_timer(2.0, hello, 0, ["juxicn"])
    t.start()
