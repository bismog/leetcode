#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import otherMod2

def main():
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    # create logger file handler
    fh = logging.FileHandler('new_snake.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s -\
        %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info('program started')
    result = otherMod2.add(7, 8)
    logger.info('done!')

if __name__ == '__main__':
    main()
