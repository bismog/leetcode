#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.config
import otherMod2

def main():
    dictLogConfig = {
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "filename": "config2.log",
                "formatter": "myFormatter"
            }
        },
        "loggers": {
            "exampleApp": {
                "handlers": [
                    "fileHandler"
                ],
                "level": "INFO"
            }
        },
        "version": 1
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger('exampleApp')

    logger.info('program started')
    result = otherMod2.add(7, 8)
    logger.info('done!')

if __name__ == '__main__':
    main()
