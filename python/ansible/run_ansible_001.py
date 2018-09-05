#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://serversforhackers.com/c/running-ansible-programmatically
# cmladd: ansible.callbacks no longer exists in 2.0
# So I reckon that this is a deprecate introduction
# For update documentation, please refer to: http://docs.ansible.com/ansible/latest/dev_guide/developing_api.html
from ansible.playbook import Playbook
from ansible.inventory import Inventory
from ansible import callbacks
from ansible import utils

import jinja2
from tempfile import NamedTemporaryFile
import os

utils.VERBOSITY = 0
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
stats = callbacks.AggregateStats()
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

# Sample inventory
inventory = '''
[customer]
{{ public_ip_address }}

[customer:vars]
domain={{ domain_name }}
customer_id={{ customer_id }}
customer_name={{ customer_name }}
customer_email={{ customer_email }}
'''

inventory_template = jinja2.Template(inventory)
# rendered_inventory = inventory_template.render({
#     'public_ip_address': '11.22.33.44',
#     'domain_name': 'some.domainname.com',
#     'customer_id': '112233',
#     'customer_name': 'customer_xxx',
#     'customer_email': 'xxx@customer.com'
# })
rendered_inventory = inventory_template.render({
    'public_ip_address': '10.43.174.158',
    'domain_name': 'lyy',
    'customer_id': '9527',
    'customer_name': 'root',
    'customer_email': 'xxx@customer.com'
})


import pdb;pdb.set_trace()
# Create a temporary file and write the template string to it
hosts = NamedTemporaryFile(delete=False)
hosts.write(rendered_inventory)
hosts.close()

pb = Playbook(
    playbook='/home/git/leetcode/ansible/playbook/config_variable_to_ini_file_003.yml',
    host_list=hosts.name,
    remote_user='root',
    callbacks=playbook_cb,
    runner_callbacks=runner_cb,
    # private_key_file='/path/to/key.pem',
    stats=stats
)

results = pb.run()

# Ensure on_stats callback is called for callback modules
playbook_cb.on_stats(pb.stats)

os.remove(hosts.name)

print results
