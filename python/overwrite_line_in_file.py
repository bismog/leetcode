#!/usr/bin/env python
# -*- coding: utf-8 -*-

def write_a_file():
    # f = open('workfile', 'w')
    with open('/tmp/workfile', 'w') as f:
        f.write("adfasdfasdfasdfadfa -1111111111111111")
        f.write("adfasdfasdfasdfadfa -1111111111111111")
        f.write("adfasdfasdfasdfadfa -1111111111111111")
        f.write("adfasdfasdfasdfadfa -1111111111111111")
        f.close()

def overwrite_line(ln):
#     with open('/tmp/workfile', 'rw') as f:
#         c = 0
#         for line in f:
#             if c == int(ln):
#                 line.replace("
    pass

# if __name__ == "__main__":
write_a_file()
overwrite_line(3, "xxxxxxxxxxxxxxxxxxxxx-   xx")
