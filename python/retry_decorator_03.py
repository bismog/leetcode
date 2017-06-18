#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from functools import wraps

def retry(exceptions=Exception, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.
    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param exception: the exception to check. may be a tuple of exceptions to 
        check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kargs):
            mtries, mdelay = tries, delay
            while mtries > 0:
                try:
                    return f(*args, **kargs)
                except exceptions as e:
                    mtries -= 1
                    if mtries == 0:
                        break
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
                    time.sleep(mdelay)
                    mdelay *= backoff
            # raise exceptions
            raise e
        return f_retry
    return deco_retry


@retry(exceptions=Exception, tries=4, delay=1)
def read_file():
    print 'read file xxx'
    raise IOError


def main():
    read_file()

if __name__ == "__main__":
    main()
