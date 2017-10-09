#!/usr/bin/env python
#-*- coding:utf-8 -*-

import netaddr
from netaddr import IPNetwork
# iplist =[
#     IPNetwork('10.105.205.8/29'), 
#     IPNetwork('10.105.205.16/28'), 
#     IPNetwork('10.105.205.32/27'), 
#     IPNetwork('10.105.205.64/26'), 
#     IPNetwork('10.105.205.128/26'),
#     IPNetwork('10.105.205.192/28'),
#     IPNetwork('10.105.205.208/29'),
#     IPNetwork('10.105.206.48/28'),
#     IPNetwork('10.105.206.80/28')
#     ]

# iplist =[
#         IPNetwork('10.105.205.8/29'), 
#         IPNetwork('10.105.205.16/28'), 
#         IPNetwork('10.105.205.32/27'), 
#         IPNetwork('10.105.205.64/26'),
#         IPNetwork('10.105.205.0/29'),
#         ]

iplist = [
        IPNetwork('209.152.214.112/30'),
        IPNetwork('209.152.214.116/31'),
        IPNetwork('209.152.214.118/31'),
]

summary = netaddr.cidr_merge(iplist)
print summary

