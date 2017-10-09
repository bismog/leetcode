#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import groupby
from operator import itemgetter

data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in groupby(enumerate(data), lambda (i, x): i-x):
    print map(itemgetter(1), g)

