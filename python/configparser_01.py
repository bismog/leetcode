#!/usr/bin/env python
#-*- coding:utf-8 -*-

import subprocess
import sys
from ConfigParser import SafeConfigParser

def main(args):
    # Copy remote conf file to localhost
    conf_file_name = args['conf'].split('/')[-1]
    replica_file = conf_file_name
    # replica_file = '/tmp/' + args['node'] + '_' + conf_file_name
    # command_cp = "scp %s:%s %s" % (args['node'], args['conf'], replica_file)
    # cp_conf = subprocess.Popen(command_cp.split(), stdout=subprocess.PIPE)
    # cp_conf.communicate()

    # Parse conf file, get specified item value
    parser = SafeConfigParser()
    parser.read(replica_file)

    result_value = parser.get(args['section'], args['item'])
    print result_value

if __name__ == "__main__":
    '''
    args = {
        "conf": "/etc/xxx/xxx.conf",
        "item": "delay",
        # "node": "10.43.174.158",
        "section": "default",
    }
    '''

    args = {
        "conf": sys.argv[1],
        "item": sys.argv[3],
        # "node": sys.argv[1],
        "section": sys.argv[2]
    }
    main(args)


