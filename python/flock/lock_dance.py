#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://github.com/derpston/python-simpleflock/blob/master/src/simpleflock.py

import fcntl
import time

fd = open('foo', 'w+')

while True:
    try:
        print(time.time())
        print 'acquiring lock...'
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        print(time.time())
        print('Lucky! I get lock')
        time.sleep(5)
        print(time.time())
        print('Done. Release lock.')

        # If we run a daemon service, we can release lock
        # via either fd.close() or fcntl.flock(fd, fcntl.LOCK_UN)
        # fd.close()
        # fcntl.flock(fd, fcntl.LOCK_UN)
        break
    except IOError as e:
        # raise on unrelated IOErrors
        print(time.time())
        print('Lock failed, continue aquiring after 1 second...')
        # if e.errno != errno.EAGAIN:
        #     raise
        # else:
        #     time.sleep(0.1)
        time.sleep(1)

