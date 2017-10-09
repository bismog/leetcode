#!/usr/bin/env python

def rotate(arr, n):
#    sp = len(arr) - n % len(arr)
#    arr = arr[sp:].__add__(arr[:sp])
    sp = -n % len(arr)
    arr = arr[sp:] + arr[:sp]
    return arr

def main():
    array_x = ['a', 'b', 'c']
    array_y = [1.0, 2.0, 3.0]
    array_z = [1, 2, 3, 4, 5]
    xo = rotate(array_x, 2)
    yo = rotate(array_y, 5)
    zo = rotate(array_z, 1)
    print xo, yo, zo


if __name__ == "__main__":
    main()
