#!/usr/bin/env python

import re

pnlist = ["1234 5678", # is valid
    "2359 1478", # is valid
    "85748475", # invalid, as there are no spaces separating the first 4 and last 4 digits
    "3857  4756", # invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
    "sklfjsdklfjsf", # clearly invalid
    "     1234 5678   ", # is NOT a valid phone number but CONTAINS a valid phone number
    "skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf", #also contains a valid HK phone number (9345 8234)
]

def isValidHKPhoneNumber(phone_number):
    p = re.compile("^\d{4} \d{4}$")
    result = p.match(phone_number)
    return True if result else False

def hasValidHKPhoneNumber(phone_number):
    p = re.compile("\d{4} \d{4}")
    result = p.search(phone_number)
    return True if result else False

def main():
    valid_out = "\"%s\" is valid phone number"
    invalid_out = "\"%s\" is invalid phone number"
    has_valid_out = ", but has valid phone number"
    not_has_valid_out = ", and has not valid phone number"
    for i in range(len(pnlist)):
        if isValidHKPhoneNumber(pnlist[i]):
            print valid_out % pnlist[i]
        else:
            print invalid_out % pnlist[i],
            print has_valid_out if hasValidHKPhoneNumber(pnlist[i]) else not_has_valid_out

if __name__ == "__main__":
    main()
