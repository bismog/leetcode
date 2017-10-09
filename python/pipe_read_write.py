#!/usr/bin/env python

import os

r,w = os.pipe()
rr = os.fdopen(r)

ww = os.fdopen(w, 'w')
ww.write("year 2015 is fantasy")
out = rr.read()

print "read: ", out
