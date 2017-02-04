#!/usr/bin/env python

import os
import sys


# print sys.argv
usage = "usage: %s search_text replace_text [infilename [outfilename]]" % \
    os.path.basename(sys.argv[0])
if len(sys.argv) < 3:
    print usage
print "This script is %s" % sys.argv[0]
print "Now we will replace %s in file %s with %s, and output to file %s." % \
    (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

infile=open(sys.argv[3])
outfile=open(sys.argv[4], 'w')

for cc in infile:
    print cc
    outfile.write(cc.replace(sys.argv[1], sys.argv[2]))
infile.close()
outfile.close()
