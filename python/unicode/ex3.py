#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

# https://pythonhosted.org/kitchen/unicode-frustrations.html
# Python even provides you with a facility to do just this. If you know that every 
# unicode string you send to a particular file-like object (for instance, stdout) 
# should be converted to a particular encoding you can use a codecs.StreamWriter 
# object to convert from a unicode string into a byte str. In particular, 
# codecs.getwriter() will return a StreamWriter class that will help you to wrap 
# a file-like object for output. Using our print() example:
import codecs
import sys

utf8writer = codecs.getwriter('utf8')
sys.stdout = utf8writer(sys.stdout)
# print 'café'
print u'café'

asciiwriter = codecs.getwriter('ascii')
sys.stdout = asciiwriter(sys.stdout)
# print u'café'
print u'cafe'
