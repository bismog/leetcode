#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    #ff = open("/tmp/aaabbb.txt", 'r')
    raise IOError, 'No file named "/tmp/aaabbb.txt" found.'
#except IOError, e:
except IOError as e:
    print "Could not open file:", e


# https://docs.python.org/2/library/subprocess.html#subprocess.check_output
# The CalledProcessError object will have the return code in the returncode 
# attribute and any output in the output attribute.
# Example: http://stackoverflow.com/questions/24849998/how-to-catch-exception-output-from-python-subprocess-check-output
import subprocess
try:
    # subprocess.check_output(['gogogo', 'boys', 'and', 'girls'])
    subprocess.check_output(['ping', '-c', '3', '111.222.123.133'])
except subprocess.CalledProcessError as e:
    # print 'EEEEE:', e.output
    pass
