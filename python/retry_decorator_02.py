#!/usr/bin/env python
#-*- coding:utf-8 -*-

from retrying import retry

@retry(wait_fixed=3, stop_max_attempt_number=5)
def read_file():
    print 'read file xxx'
    raise Exception
    # return -1


def main():
    try:
        read_file()
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
