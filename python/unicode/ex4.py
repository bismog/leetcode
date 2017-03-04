#!?usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from kitchen.text.converters import getwriter

utf8writer = getwriter('utf8')
sys.stdout = utf8writer(sys.stdout)
print u'café'
print 'café'
