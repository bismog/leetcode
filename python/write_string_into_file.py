#!/usr/bin/env python

content_model = \
'''authoritative;
ddns-update-style interim;
allow booting;
allow bootp;
next-server 129.128.0.1;
filename "pxelinux.0";

default-lease-time 1800;
max-lease-time 7200;
ping-check true;
option domain-name-servers 129.128.0.1;

subnet 129.128.0.0 netmask 255.255.255.0
{
        range 129.128.0.3  129.254.254.254;
        option routers 129.128.0.1;
        option broadcast-address 129.128.255.255;
}
'''

fo = open("/tmp/whatever_you_like", 'w')
fo.write(content_model)
fo.close()
