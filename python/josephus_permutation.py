#!/usr/bin/env python


def josephus(circle, m):
    away = []
    i = 0

    while len(circle) > 0:
        i = (i+m-1)%len(circle)
        away.append(circle.pop(i))
    return away


suicide_circle = [1,2,3,4,5,6,7]

if __name__ == "__main__":
    print josephus(suicide_circle, 3)
