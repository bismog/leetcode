#!/usr/bin/env python

import re

class String(object):
    def to_integer(self, ss):
        p = [r'[+,-]?\d+', r'[+,-]?\\b[01]+', r'[+,-]?\\o[0-7]+', r'[+,-]?\\x[0-9a-fA-F]+']
        ps = '|'.join(p)
        r = re.compile(ps)
        matched_pattern = r.match(ss)
        # if matched_pattern:
        #     out = None
        #     try:
        #         out = int(ss)
        #     except ValueError:
        #         pass
        # return out
        if matched_pattern:
            return matched_pattern.group()
        else:
            return None
        #return int(ss, base=0) if matched_pattern else None

input_string = [
    "0xb3", "+33", "-0b1011", "0b1,", "+0o12", "a3", "++5", "-+7", "--0xaa", "0x+13", "0b-110"
]

if __name__ == "__main__":
    s2i = String()
    outs = []
    for x in range(len(input_string)):
        outs.append(s2i.to_integer(input_string[x]))
    print outs
    
