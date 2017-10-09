#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scapy.all import srp,Ether,ARP,conf,get_if_hwaddr,get_if_addr
import time

#ipscan='192.168.1.1/24'
ipscan='10.43.211.1/24'


import socket
import fcntl
import struct

def ip_conflict():
    start = time.clock()
    # print "start time", start
    ip_dict = dict()
    conf = False
    ip_me = get_if_addr('eth0')
    mac_me = get_if_hwaddr('eth0')
    ip_dict[ip_me] = mac_me
    while True:
        end = time.clock()
        # print "endtime",end
        # print "??:"
        # print int(end-start)
        if int(end-start) > 1:
            # print ('Timeout!!!')
            break
        try:
            ans,unans=srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan),timeout=2,verbose=False)
        except Exception,e:
            print str(e)
        else:
            print ("   MAC            --   IP   ")
            for snd,rcv in ans:
                list_mac=rcv.sprintf("%Ether.src% -- %ARP.psrc%")
                mac = rcv.sprintf("%Ether.src%")
                ip = rcv.sprintf("%ARP.psrc%")
                if ip not in ip_dict:
                    ip_dict[ip] = mac
                else:
                    if mac != ip_dict[ip]:
                        print "*************IP collision found***************"
                        if ip == ip_me:
                            print "IP address:",ip
                            print "IP collision found with local machine"
                            print "MAC of collided machine:",mac_me,ip_dict[ip]
                            conf = True
                        else:    
                            print ""
                            print "IP address:",ip
                            print "MAC of collided machine:",mac,ip_dict[ip]
                            conf = True
                        print "*****************************************"
                print list_mac
    print "\nIP address, MAC address mapping table"
    print "    ip               MAC"
    for has_ip in ip_dict.keys():
        print has_ip, "------ " + ip_dict[has_ip]
    if conf is True:
        print "\nµno IP collision found.\n"

    print "\nall IP in current LAN list as below:"
    for has_ip in ip_dict.keys():
        print has_ip
    print "\nÈprint avoid the same IP as mesioned above.\n"

print "Welcome to IP_collision_checking..."
print "This code script can find all the IP collision in current LAN, also can list all the IP in it.\n\n"
print "Okay, let's begin:"
ip_conflict()
# print get_if_hwaddr('wlan0')
# print get_if_addr('wlan0')
# print "byebye"
