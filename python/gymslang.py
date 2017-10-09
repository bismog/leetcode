#!/usr/bin/env python
import re

def gymslang(str):
    for k,v in ss_map.items():
        p = re.compile(k)
        str = p.sub(v, str)
    return str

ss = " probably Probably prolly Prolly i am I am i'm I'm instagram Instagram insta Insta do not Do not don't Don't going to Going to gonna Gonna combination Combination combo Combo "
ss_map = {
    "probably": "prolly",
    "Probably": "Prolly",
    "i am": "i'm",
    "I am": "I'm",
    "instagram": "insta",
    "Instagram": "Insta",
    "do not": "don't",
    "Do not": "Don't",
    "going to": "gonna",
    "Going to": "Gonna",
    "combination": "combo",
    "Combination": "Combo"
}


def main():
    ss_slang = gymslang(ss)
    print ss_slang

if __name__ == "__main__":
    main()
