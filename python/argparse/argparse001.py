#!/usr/bin/env python

# import argparse
# 
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
# 
# args = parser.parse_args()
# print(args.accumulate(args.integers))

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    #parser.print_help()

if __name__ == "__main__":
    main()