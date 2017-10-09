#!/usr/bin/env python
import itertools

def multiiter(*params):
    py = 1
    if len(params) == 1:
        px = params[0]
    else:
        px = params[0]
        py = params[1]
    # for x in itertools.combinations(range(px), pn):
    # for x in itertools.permutations(range(px), pn):
    # for x in itertools.combinations_with_replacement(range(px), pn):
    for x in range(px):
        if py == 1:
            yield(x, )
        else:
            for y in range(py):
                yield (x, y)

def main():
    print list(multiiter(0))
    print list(multiiter(2))
    print list(multiiter(3))
    print list(multiiter(1,2))
    print list(multiiter(3,1))
    print list(multiiter(3,2))
    print list(multiiter(2,3))

if __name__ == "__main__":
    main()
