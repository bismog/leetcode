#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import sys

fi = open('./bismog_utf8.txt', 'r')
bismog_utf8 = fi.read()
print bismog_utf8
print type(bismog_utf8)

bismog_uni = bismog_utf8.decode('utf-8')
print bismog_uni
print type(bismog_uni)

fo = open('/tmp/bismog.txt', 'w')
# fo.write(bismog_uni)
# fo.write(bismog_uni.encode())
# fo.write(bismog_uni.encode(sys.getdefaultencoding()))
fo.write(bismog_uni.encode('utf-8'))


def to_unicode_or_bust(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

print to_unicode_or_bust(bismog_utf8)
print to_unicode_or_bust(bismog_uni)
print to_unicode_or_bust(1234)

