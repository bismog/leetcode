#!/usr/bin/env python

from __future__ import print_function
from oslo.config import cfg

# here name 'simple' should match with section name in *.conf
opt_group = cfg.OptGroup(name='simple', title='A Simple Example')  # format: name + title
simple_opts = [cfg.BoolOpt('enable', default=False, help=('True enables, False disables')),
               cfg.StrOpt('xxx', default="xxx.default", help=('... ...')) 
              ]  # format: name + default + help

test_group = cfg.OptGroup(name='default', title='A Default Example')  # format: name + title
test_opts = [
        cfg.StrOpt('topic',
                    default='this is a test value',
                    help='this is a test config'),
        cfg.StrOpt('say',
                    default='world',
                    help=' jkjk ')
        ]
 
CONF = cfg.CONF
#CONF.register_group(opt_group)
#CONF.register_opts(simple_opts, opt_group)
CONF.register_group(test_group)
CONF.register_opts(test_opts, test_group)

if __name__ == "__main__":
    CONF(default_config_files=['app.conf'])
    #print(CONF.simple.enable)     #cmladd: here will print True
    #print(CONF.simple.xxx)
    print(CONF.default.topic)
    print(CONF.default.say)

