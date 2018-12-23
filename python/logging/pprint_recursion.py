#!/usr/bin/env python

from pprint import pprint
from copy import copy


local_data = ['a', 'b', 1, 2]
remote_data = copy(local_data)

local_data.append(local_data)
remote_data.extend(remote_data)

print('id(local_data)=>', id(local_data))
print
print(local_data)
print
pprint(local_data)

print(remote_data)
