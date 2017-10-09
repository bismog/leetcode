#!/usr/bin/python

import sys
import libnet
from libnet.constants import * 

# params:1 - The injection type, 2 - Device name
l = libnet.context(LINK, 'eth0')
# Let's get the network byte ordered representation of this IP
dst_ip = l.name2addr4('10.0.0.9', DONT_RESOLVE)

dst='ffffffffffff'
dst_mac = dst.decode("hex")
src='001d92e08f26'
src_mac = src.decode("hex")
arp_tag = l.autobuild_arp(1, src_mac, dst_ip, dst_mac, dst_ip,)

eth_tag =  l.autobuild_ethernet(dst_mac, 0x0806,)

# Now let's write the packet and check for an error
# tcp syn google.com
import time
while 1:
        time.sleep(10)
        l.write()
#l.write()
