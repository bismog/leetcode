#!/usr/bin/env python
import socket
import time
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('127.0.0.1',8123))
ss.sendall('Now client connect to Server')
aa=ss.recv(1024)
print aa
while True:
    username=raw_input('-->username:').strip()
    ss.sendall('username:'+username)
    re=ss.recv(1024)
    if re=='valid':
        break
    else:
        print "username Error,try again"
        continue
while True:
    userpasswd=raw_input('-->userpasswd:').strip()
    ss.sendall('userpasswd:'+userpasswd)
    re=ss.recv(1024)
    if re=='valid':
        print ss.recv(1024)
        break
    else:
        print 'userpasswd Error,try again'
        continue
if ss.recv(3)=='FOE':
    ss.close()
    print 'over!'
