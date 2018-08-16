#!/usr/bin/env python

def find_longest_substring(raw):
    if not raw:
        return 0,None
    if len(raw) == 1:
        return 1,raw
    # i = left = cur_len = max_len = 0
    i, left, cur_len, max_len = 0, 0, 0, 0
    sub = ''
    collected_sub = {}
    max_sub = []
    char_dict = {}
    while i<len(raw):
        check_index = char_dict.get(raw[i])
        if check_index:
            if check_index < left:
                # sub += raw[i]
                sub = raw[left:i]
                cur_len += 1
            else:
                left = check_index + 1
                sub = raw[left:i]
                cur_len = i-left+1
        else:
            # sub += raw[i]
            sub = raw[left:i]
            cur_len += 1

        if cur_len >= max_len:
            max_len = cur_len
            collected_sub[sub] = max_len
        char_dict[raw[i]] = i
        i += 1

    for k,v in collected_sub.items():
        if v == max_len:
            max_sub.append(k)
    return max_len, max_sub

def main():
    raw_string = "abcdcafbkgzjaf"
    max_len,sub = find_longest_substring(raw_string)
    print "maximum length of longest substring is: %d, it's %s." % (max_len, sub)

if __name__ == "__main__":
    main()
