#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)

log = logging.getLogger('ex')

try:
    raise RuntimeError
# except Exception, err:
#     log.exception('Error')
except RuntimeError:
    log.exception('RuntimeError')
