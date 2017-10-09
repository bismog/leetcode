#!/usr/bin/env python
from mock import Mock, MagicMock

class ProductionClass(object):
    pass

thing = ProductionClass()
#thing.method = MagicMock(return_value =3)
thing.method = Mock(return_value =3)
result = thing.method(3,4,5,key='value')
print result
thing.method.assert_called_with(3,4,5,key='value')
