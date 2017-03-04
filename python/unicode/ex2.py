#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
fi = codecs.open('./bismog_utf8.txt', 'r', encoding='utf-8')
bismog_uni = fi.read()
fi.close()

# bismog_uni = u'Bismog Cheng\u8302\u6797\n'
fo = codecs.open('/tmp/bismog.txt', 'w', encoding='utf-8')
fo.write(bismog_uni)
fo.close()


