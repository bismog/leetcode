#!/usr/bin/python
import os
import tempfile
import errno

fd, tmpname = tempfile.mkstemp()
fo = os.fdopen(fd, "w")
fo.write("something\n")
fo.close()
try:
    os.close(fd)
except OSError as oserr:
    if oserr.args[0] == errno.EBADF:
            print ("Closing file has closed file descriptor.")
    else:
        print ("Some other error:", oserr)
else:
    print ("File descriptor not closed.")
