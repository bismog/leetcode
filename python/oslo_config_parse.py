#!/usr/bin/env python

from oslo.config import cfg
import sys
 
test_group = cfg.OptGroup(name='default', title='A Default Example')  # format: name + title
test_opts = [
        cfg.StrOpt('topic',
                    default='this is a test value',
                    help='this is a test config'),
        cfg.StrOpt('say',
                    default='world',
                    help=' jkjk ')
        ]
 
#def parse_argv(argv, default_config_files=None):
#    cfg.CONF(argv[1:], project='test',
#            default_config_files=default_config_files)
 
CONF=cfg.CONF
CONF.register_group(test_group)
CONF.register_opts(test_opts, test_group)
#CONF.register_opts(test_opts)

if __name__ == "__main__":
    #CONF(sys.argv[1:], project='test', default_config_files=['test.conf'])
    CONF(default_config_files=['test.conf'])
    print CONF.default.topic
    print CONF.default.say
    #print CONF.topic
    #print CONF.say
