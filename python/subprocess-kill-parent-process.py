#!/usr/bin/env python


from subprocess import Popen

count = 0

while True:
    print 'good day %d ...' % count
    count = count + 1
    if count == 20000:
        print "20000, flag it"
        # sucide = Popen("pkill -9 -f subprocess-kill-parent-process.py", shell=True)
        sucide = Popen("pkill -9 -f subprocess-kill-parent-process.py", shell=False)
        status = sucide.wait()
        if status == 0:
            print "you see this came from mystery process"
        else:
            print "how can this be?"

