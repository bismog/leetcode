#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ansible.compat.tests import unittest
from ansible.compat.tests.mock import call,create_autospec,patch,mock_open
from ansible.module_utils.basic import AnsibleModule

from write_your_first_module import wyfm

class TestFirstMod(unittest.TestCase):
    
    @patch('write_your_first_module.wyfm.write')
    @patch('write_your_first_module.wyfm.fetch')
    def test__save_data__happy_path(self, fetch, write):
        # Setup
        mod_cls = create_autospec(AnsibleModule)
        mod = mod_cls.return_value
        mod.params = dict(
            url='www.google.com',
            dest='/tmp/firstmod.txt'
        )

        # Exercise
        wyfm.save_data(mod)

        # Verify
        self.assertEqual(1, fetch.call_count)
        expected = call(mod.params['url'])
        self.assertEqual(expected, fetch.call_args)

        self.assertEqual(1, write.call_count)
        expected = call(fetch.return_value, mod.params['dest'])
        self.assertEqual(expected, write.call_args)

        self.assertEqual(1, mod.exit_json.call_count)
        expected = call(msg='Data saved', changed=True)
        self.assertEqual(expected, mod.exit_json.call_args)

    @patch('write_your_first_module.open_url')
    def test__fetch__happy_path(self, open_url):
        # Setup
        url = 'https://www.google.com'

        # Mock the return value of open_url
        stream = open_url.return_value
        stream.read.return_value = "<html><head></head><body>Hello</body></html>"
        stream.getcode.return_value = 200
        open_url.return_value = stream

        # Exercise
        data = wyfm.fetch(url)

        # Verify
        self.assertEqual(stream.read.return_value, data)
        self.assertEqual(1, open_url.call_count)
        expected = call(url)
        self.assertEqual(expected, open_url.call_args)
