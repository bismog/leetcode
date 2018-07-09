import collections

d = dict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
d['f'] = 'F'


od = collections.OrderedDict()
od['a'] = 'A'
od['b'] = 'B'
od['c'] = 'C'
od['d'] = 'D'
od['e'] = 'E'
od['f'] = 'F'

for k,v in d.items():
    print k,v

for k,v in od.items():
    print k,v
