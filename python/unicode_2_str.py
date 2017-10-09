#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ast
import json
import collections

literal_dict = {'tecsclient_vip': u'172.255.200.18', 'provider_public_vip': u'172.255.201.18', 'networks': [{'id': u'9c5454f4-a245-4066-be52-d44ad6160e45', 'vlan_id': u'803', 'ip_ranges': [{u'start': u'172.255.201.15', u'cidr': u'172.255.201.0/24', u'end': u'172.255.201.16', u'gateway': u''}]}, {'ips': [{u'ip': u'172.255.200.15', u'host_name': u'Controller0115'}, {u'ip': u'172.255.200.16', u'host_name': u'Controller0116'}], 'netmask': u'255.255.255.0', 'id': u'7639b96e-3f2f-46da-a0b0-c0dbb515dd6e', 'vlan_id': u'802', 'ip_ranges': [{'start': '', 'end': '', 'gateway': u''}]}, {'ips': [{u'ip': u'10.43.20.172', u'host_name': u'Controller0115'}, {u'ip': u'10.43.20.173', u'host_name': u'Controller0116'}], 'netmask': u'255.255.254.0', 'id': u'52c37ea7-9cb4-47d7-aa0f-2aedd8e8ab86', 'vlan_id': u'700', 'ip_ranges': [{'start': '', 'end': '', 'gateway': u'10.43.20.1'}]}], 'outband_vip': u'10.43.20.177', 'public_vip': u'172.255.201.17'}

# print literal_dict
# obj = json.loads(literal_dict)
# print obj

# DATA = { u'spam': u'eggs', u'foo': frozenset([u'Gah!']), u'bar': { u'baz': 97 },
#          u'list': [u'list', (True, u'Maybe'), set([u'and', u'a', u'set', 1])]}

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

print literal_dict
print convert(literal_dict)
# Prints:
# {u'list': [u'list', (True, u'Maybe'), set([u'and', u'a', u'set', 1])], u'foo': frozenset([u'Gah!']), u'bar': {u'baz': 97}, u'spam': u'eggs'}
# {'bar': {'baz': 97}, 'foo': frozenset(['Gah!']), 'list': ['list', (True, 'Maybe'), set(['and', 'a', 'set', 1])], 'spam': 'eggs'}
