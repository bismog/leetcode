#!/usr/bin/python

import copy

mydict = {'name': 'foobar', 'data': [1, 2, 3]}

copy_dict=mydict
shallow_dict=copy.copy(mydict)
deep_dict=copy.deepcopy(mydict)

if(id(copy_dict) == id(mydict)):
    print 'id of copy_dict and mydict is same'
else:
    print 'id of copy_dict and mydict is not same'

if(id(copy_dict['name']) == id(mydict['name'])):
    print 'id["name"] of copy_dict and mydict is same'
else:
    print 'id["name"] of copy_dict and mydict is not same'

if(id(copy_dict['data']) == id(mydict['data'])):
    print 'id["data"] of copy_dict and mydict is same'
else:
    print 'id["data"] of copy_dict and mydict is not same'



if(id(shallow_dict) == id(mydict)):
    print 'id of shallow_dict and mydict is same'
else:
    print 'id of shallow_dict and mydict is not same'

if(id(shallow_dict['name']) == id(mydict['name'])):
    print 'id["name"] of shallow_dict and mydict is same'
else:
    print 'id["name"] of shallow_dict and mydict is not same'

if(id(shallow_dict['data']) == id(mydict['data'])):
    print 'id["data"] of shallow_dict and mydict is same'
else:
    print 'id["data"] of shallow_dict and mydict is not same'
                                                             



if(id(deep_dict) == id(mydict)):
    print 'id of deep_dict and mydict is same'
else:
    print 'id of deep_dict and mydict is not same'

if(id(deep_dict['name']) == id(mydict['name'])):
    print 'id["name"] of deep_dict and mydict is same'
else:
    print 'id["name"] of deep_dict and mydict is not same'

if(id(deep_dict['data']) == id(mydict['data'])):
    print 'id["data"] of deep_dict and mydict is same'
else:
    print 'id["data"] of deep_dict and mydict is not same'
                                                          
if(id(deep_dict['data'][0]) == id(mydict['data'][0])):
    print 'id["data"][0] of deep_dict and mydict is same'
else:
    print 'id["data"][0] of deep_dict and mydict is not same'

