#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://pythonhosted.org/kitchen/unicode-frustrations.html
# raising exceptions really cannot handle non-ASCII characters in a unicode 
# string and will output an exception without the message if the message contains them.

# import sys
# from kitchen.text.converters import getwriter
# 
# utf8writer = getwriter('utf8')
# sys.stderr = utf8writer(sys.stderr)

from kitchen.text.converters import to_bytes

class MyException(Exception):
    pass

# def to_bytes(unistr):
#     return unistr.encode('utf8')

# This is just okay, Does this mean Exception accept arguments 'str' other 
# than 'unicode'?
# raise MyException(to_bytes(u'Cannot do this'))   

# raise MyException('Cannot do this while at a café')
raise MyException(to_bytes(u'Cannot do this while at a café'))
