#!/usr/bin/env python
#-*- coding:utf-8 -*-

import argparse
# parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser = argparse.ArgumentParser()
parent_parser.add_argument('--parent', type=int)
# parent_parser.parse_args()

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
# foo_parser.add_argument('foo')
# foo_parser.parse_args(['--parent', '2', 'XXX'])
foo_parser.parse_args()
# 
# bar_parser = argparse.ArgumentParser(parents=[parent_parser])
# bar_parser.add_argument('--bar')
# bar_parser.parse_args(['--bar', 'YYY'])

# bar_parser.print_help()
