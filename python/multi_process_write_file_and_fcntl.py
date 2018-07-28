#!/usr/bin/env python

import multiprocessing
import time
import random
import fcntl

def match_or_update(filename, keyword):
    with open(filename, 'a+') as fp:
        fcntl.flock(fp, fcntl.LOCK_EX)
        flines = fp.readlines()

        matched =False
        for line in flines:
            if keyword in line:
                matched = True
                break

        append_line = '\n'
        changed = False
        if not matched:
            append_line = '\n' + '+ ' + keyword
            # flines.append(append_line)
            changed = True

        if changed:
            # time.sleep(random.randint(0,5))
            # fw.writelines(flines)
            fp.writelines(append_line)

        fcntl.flock(fp, fcntl.LOCK_UN)
    

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
