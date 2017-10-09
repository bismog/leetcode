#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: pexpect_test.py
'''
Created on 2010-7-2
 
@author: forever
'''
import pexpect
 
if __name__ == '__main__':
    user = 'root'
    ip = '10.43.114.54'
    mypassword = 'ztescs'
 
    print user
    child = pexpect.spawn('ssh %s@%s' % (user,ip))

#    child.expect('(yes/no)?')
#    child.sendline("yes\r")

    child.expect('password:')
    child.sendline (mypassword)
 
    child.expect('$')
#    child.expect('#')
    child.sendline('sudo -s')
    child.expect(':')
    child.sendline (mypassword)
    child.expect('#')
    child.sendline('ls -la')
    child.expect('#')
    print child.before   # Print the result of the ls command.
    child.sendline("echo '112' >> /home/chml/1-by-pexpect.txt ")
    child.interact()     # Give control of the child to the user.
 
    pass
