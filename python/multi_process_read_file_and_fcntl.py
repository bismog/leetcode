#!/usr/bin/env python

import multiprocessing
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
    ps = []
    for i in range(instances):
        p = multiprocessing.Process(target=match_or_update, args=(filename, keyword))
        ps.append(p)

    for p in ps:
        p.start()

    for p in ps:
        p.join()

def main():
    filename = '/run/xxx'
    keyword = 'kangaroo'
    instances = 8
    multi_handlers(filename, keyword, instances)

if __name__ == "__main__":
    main()
