#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

whatever_you_say = sys.argv[1]
host = 'localhost'
port = 18081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.sendto(whatever_you_say, (host, port))
