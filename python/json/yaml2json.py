#!/usr/bin/env python
# -*- coding:utf-8 -*-

# From yaml file to json file
import json,yaml
with open('xxx.yaml', 'r') as yf:
    loaded_yaml = yaml.load(yf)
with open('xxx.json', 'w') as jf:
    json.dump(loaded_yaml, jf)    ## Alternatively, json.dump(loaded_yaml, json_file, indent=4)

