#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.config
import otherMod2

def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    logger.info('progress started')
    result = otherMod2.add(7, 8)
    logger.info('done!')

if __name__ == '__main__':
    main()
