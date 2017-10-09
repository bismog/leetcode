#!/usr/bin/env python

import os,sys

r,w = os.pipe()
pid = os.fork()  #Return 0 to child process and PID of child to parent process
if pid:
    #parent process
    os.close(w)   #parent process read from pipe
    r = os.fdopen(r)
    print "parent: reading..."
    txt = r.read()
    os.waitpid(pid, 0)
else:
    os.close(r)  #chile process write to pipe
    w = os.fdopen(w,'w')
    print "child: writing..."
    w.write("fucking GFW")
    w.close()
    print "child: closing"
    sys.exit(0)

print "parent received: ", txt
