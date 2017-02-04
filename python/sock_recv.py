#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# server.py
import socket
port = 18081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print "waiting on port:", port
while 1:
    data, addr = s.recvfrom(1024)
    print data
