#!/usr/bin/env python

import site

plists = site.getsitepackages()
for x in range(len(plists)):
    print plists[x]
