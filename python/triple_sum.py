#!/usr/bin/env python

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def triple_sum(array, target):
    outs = []
    for i in range(len(array)):
        a = array[i]
        sub_target = target - a
        sub_array = array[i+1:]
        for sa in sub_array:
            complement = sub_target - sa
            if complement in sub_array and \
                sub_array.index(complement) != sub_array.index(sa) and \
                a != sa and \
                sa != complement and \
                a != complement:
                item = list(uniq(sorted([a, sa, complement])))
                if item not in outs:
                    outs.append(item)
    return outs

def main():
    array = [-1,0,1,2,-1,-4]
    target = 0
    outs = triple_sum(array, target)
    for o in outs:
        print(o[0], o[1], o[2])

if __name__ == "__main__":
    main()
