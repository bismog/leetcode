#!/usr/bin/python

fo=file("beautifulsoup4-4.2.1.tar.gz", 'r')
magic_code = fo.read(2)
if(magic_code == '\037\213'):
    print 'this is a gzip file'
else:
    print 'this is not a gzip file'

