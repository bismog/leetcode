#!/usr/bin/env python

k_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

x = 34

v_i = 119
v_t = []

factor = v_i
while factor > x:
    t = factor / x
    remainder = factor % x
    v_t.append(remainder)
    factor = t
v_t.append(factor)

v_t.reverse()
v_o = []
for t in v_t:
    v_o.append(k_list[t])

print v_o

