#!/usr/bin/env python
<<<<<<< 5fed5225edd76195f83e144ba9b02804456ac6c0
#-*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)
=======
# -*- coding:utf-8 -*-

# http://www.pythonforbeginners.com/argparse/argparse-tutorial
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('echo', help='echo the string you use here')
parser.add_argument('square', help='display a square of a given number', type=int)
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()
print(args.echo)
print(args.square**2)
if args.verbose:
    print('verbosity turned on')


>>>>>>> 9.24-10.13
