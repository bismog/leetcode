#!/usr/bin/env python

import re

def get_val(str, key):
    ''' get value of a option from a line string. '''
    pos = 0
    tmp_str = ""
    for op_str in str:
        if cmp(op_str, key):
            pos = pos + 1
        else:
            val_pos = pos + 1
            # ignore semicolon at the end of a line in isc config file 
            if str[val_pos][-1] == ';':
                tmp_str = str[val_pos][:-1]
            else:
                tmp_str = str[val_pos]
    return {key: tmp_str}


def op_get(fname, key):
    fo = open(fname)
    op_strs = []
    op_val = ""
    for line in fo:
        if re.search(key, line):
            op_strs = line.split()
            break
    if op_strs:
        op_val = get_val(op_strs, key)[key]

    fo.close()
    return op_val
    

def op_replace(fname, key, val_a, val_b):
    fo_r = open(fname, 'r')
    whole_str = ""
    for line in fo_r:
        if re.search(key, line):
            line = line.replace(val_a, val_b)
            whole_str += line
        else:
            whole_str += line
    fo_r.close()
    if whole_str:
        fo_w = open(fname, 'w')
        fo_w.write(whole_str)
        fo_w.close()

def op_set(fname, key, val):
    fo_r = open(fname, 'r')
    whole_str = ""
    for line in fo_r:
        if re.search(key, line):
            op_strs = line.split()
            if op_strs:
                old_val = get_val(op_strs,key)[key]
                line = line.replace(old_val, val)
        whole_str += line
    fo_r.close()
    if whole_str:
        fo_w = open(fname, 'w')
        fo_w.write(whole_str)
        fo_w.close()

config_file = "/etc/dhcp/dhcpd.conf"
routers = op_get(config_file, "routers")
print routers
#op_replace(config_file, "routers", routers, "192.168.1.1")
op_set(config_file, "routers", "192.168.20.1")
op_set(config_file, "routers", "192.168.20.1")

