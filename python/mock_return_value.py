#!/usr/bin/env python
from mock import Mock

mockFoo = Mock(return_value = 100)
ret = mockFoo()
print ret   #return 100
