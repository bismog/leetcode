#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

def slice_count_0(n):
    cc = int(n)
    if cc == 0:
        return 1
    else:
        return slice_count_0(cc-1) + cc

def slice_count(n):
    cc = int(n)
    return cc * (cc + 1) / 2 + 1

# for x in range(20):
#     cnt = slice_count(x)
#     print "%d:  %d" % (x, cnt)

def main():
    cnt = slice_count(sys.argv[1])
    print "%s:  %s" % (sys.argv[1], cnt)
    
if __name__ == "__main__":
    main()
