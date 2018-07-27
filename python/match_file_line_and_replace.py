#!/usr/bin/env python

import os

def ns(s):
    return s.replace(' ', '')

def match_line(a, b):
    al,_,ar = a.partition('=')
    bl,_,br = b.partition('=')
    if ns(al) == ns(bl) and ns(ar) == ns(br):
        return 'key_and_value'
    elif ns(al) == ns(bl):
        return 'key'
    else:
        return 'none'

def main():
    filename = '/run/xxx'
    key = 'abc'
    value = '123'

    if not os.path.exists(filename):
        printf("sorry, file not exist")
        pass
    with open(filename, 'r') as fr:
        file_lines = fr.readlines()

    matched = False
    changed = False
    assignment_line = '%s = %s' % (key, value)
    for index, line in enumerate(file_lines):
        if line.strip().startswith('#'):
            continue
        match_level = match_line(assignment_line, line)
        if match_level == 'key':
            matched = True
            try:
                file_lines[index] = assignment_line
                changed = True
            except:
                pass
        elif match_level == 'key_and_value':
            # It's fine already
            matched = True
            pass
        else:
            continue

    if not matched:
        file_lines.append('\n')
        file_lines.append(assignment_line)
        changed = True

    if not changed:
        pass
    else:
        with open(filename, 'w') as fw:
            fw.writelines(file_lines)

if __name__ == "__main__":
    main()
