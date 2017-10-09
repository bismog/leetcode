#!/usr/bin/env python

ddd = {'a': 111,
       'cpu': {
         'cores': 4, 'freq': 1000, 'type': 'celeron'
        },
       'storage': 222
      }

def xxx(obj):
    cpu = obj.get('cpu')
    cpu['type'] = 'xeon'

xxx(ddd)
print ddd['cpu']['type']
