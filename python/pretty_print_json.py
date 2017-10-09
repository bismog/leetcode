#!/usr/bin/env python

import json
import textwrap

your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
# parsed = json.loads(your_json)
#print json.dumps(parsed, indent=4, sort_keys=True)
# print json.dumps(parsed, indent=2)
# print textwrap.fill(your_json, 15)
print textwrap.wrap(your_json, 15)
