#!/usr/bin/env python

def find_outlier(integers):
#    odd = even = 0
#    for i in range(3):
#        if integers[i]%2 != 0:
#            odd += 1
#        else:
#            even += 1
#    find_odd = True if odd<even else False
#    for i in integers:
#        if (find_odd and i%2 != 0) or (not find_odd and i%2 == 0):
#            return i
    odds = [x for x in integers if x%2!=0]
    evens= [x for x in integers if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


def main():
    ll = [2, 4, 0, 100, 4, 11, 2602, 36]
    # ll = [160, 3, 1719, 19, 11, 13, -21]
    o = find_outlier(ll)
    print o

if __name__ == "__main__":
    main()
