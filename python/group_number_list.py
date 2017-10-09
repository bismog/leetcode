#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://codereview.stackexchange.com/questions/5196/grouping-consecutive-numbers-into-ranges-in-python-3-2
# https://stackoverflow.com/questions/2361945/detecting-consecutive-integers-in-a-list

from itertools import groupby, count
from operator import itemgetter
# import json

# groupby(numberlist, lambda n, c=count(): n-next(c))
# Then to finish it off, generate the string from the groups.

def as_range(iterable): # not sure how to do this part elegantly
    """
    # lll = [2,3,4,5,6]
    # lllo = as_range(lll)
    # print lllo
    # 
    # xxx = [3]
    # xxxo = as_range(xxx)
    # print xxxo
    """
    l = list(iterable)
    if len(l) > 1:
        return '{0}-{1}'.format(l[0], l[-1])
    else:
        return '{0}'.format(l[0])

def group_number(number_list):
    # '1-3,6-7,10'
    # raw_numberlist = [1,2,3,3,3,6,12,13,14,15,8,9,16,17,18,19]
    n_list = sorted(list(set(number_list)))
    ## This two line are the same
    # n_group = ','.join(as_range(g) for _, g in groupby(n_list, key=lambda n, c=count(): n-next(c)))
    n_group = ','.join(as_range(map(itemgetter(1), g)) for k, g in groupby(enumerate(n_list), lambda (i, x): i-x))
    return n_group

def list_number_str(number_group):
    '''
    number_group = '1-3,5,7-10'
    '''
    g_list = []
    for ran in number_group.split(','):
        if '-' not in ran:
            g_list.append(ran)
        else:
            ll,ss,rr=ran.partition('-')
            # l_group = l_group + ',' + ','.join(str(d) for d in range(int(ll),int(rr)+1))
            g_list.append(','.join(str(d) for d in range(int(ll),int(rr)+1)))
    l_group = ','.join(g for g in g_list)
    # return json.loads(l_group)
    return l_group

def list_number(number_group):
    '''
    number_group = '1-3,5,7-10'
    '''
    g_list = []
    for ran in number_group.split(','):
        if '-' not in ran:
            g_list.append(int(ran))
        else:
            ll,ss,rr = ran.partition('-')
            g_list.extend(range(int(ll), int(rr)+1))
    return g_list

raw_numberlist = [1,2,3,3,3,6,12,13,14,15,8,9,16,17,18,19]
ggo = group_number(raw_numberlist)
print ggo
llo = list_number(ggo)
print llo

