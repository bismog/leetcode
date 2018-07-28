#!/usr/bin/env python

import threading
import time
import random

def match_or_update(filename, keyword):
    with open(filename, 'r') as fr:
        flines = fr.readlines()

    matched =False
    for line in flines:
        if keyword in line:
            matched = True
            break
    append_line = '\n'
    if not matched:
        append_line = '\n' + '+ ' + keyword
        flines.append(append_line)

    time.sleep(random.randint(0,10))

    with open(filename, 'a') as fw:
        # fw.writelines(flines)
        fw.writelines(append_line)
    

def multi_handlers(filename, keyword, instances):
    ts = []
    for i in range(instances):
        t = threading.Thread(target=match_or_update, args=(filename, keyword))
        ts.append(t)

    for t in ts:
        t.start()

    for t in ts:
        t.join()

def main():
    filename = '/run/xxx'
    keyword = 'kangaroo'
    instances = 8
    multi_handlers(filename, keyword, instances)

if __name__ == "__main__":
    main()
