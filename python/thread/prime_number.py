#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading

class PrimeNumber(threading.Thread):
    # prime_numbers = {}
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
        self.lock.acquire()
        self.prime_numbers = {}
        self.lock.release()

    def run(self):
        counter = 2
        res = True
        while counter * counter < self.number:
            if self.number % counter == 0:
                res = False
            counter += 1
        self.lock.acquire()
        self.prime_numbers[self.number] = res
        self.lock.release()    
        if self.prime_numbers[self.number]:
            print "number %d is a prime number." % self.number
        else:
            print "sorry, %d isn't a prime number." % self.number

threads = []
while True:
    input = long(raw_input('number: '))
    if input < 1:
        break

    thread = PrimeNumber(input)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()
