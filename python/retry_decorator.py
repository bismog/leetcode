#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://stackoverflow.com/questions/21786382/pythonic-way-of-retry-running-a-function
# https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/

from functools import wraps

def retry(count=10):
    def decorator(func):
        @wraps(func)
        def result(*args, **kargs):
            for _ in range(count):
                try:
                    return func(*args, **kargs)
                except Exception as e:
                    sleep(2)
                    pass
        return result
    return decorator
        

@retry(count=5)
def read_file():
    print 'read file xxx'
    raise Exception


def main():
    read_file()

if __name__ == "__main__":
    main()
