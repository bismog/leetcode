#!/usr/bin/env python
# coding=utf-8

class Linux (object):
    name = 'linux'
    hardware = {'cpu': 'intel' , 'disk': '500G'}


l1 = Linux()
l1.name = 'CentOS'
l1.hardware['cpu'] = 'amd'
#l1.hardware = {'cpu' : 'amd', 'disk' :'222G'}

l2 = Linux()
print l2.name, l2.hardware

