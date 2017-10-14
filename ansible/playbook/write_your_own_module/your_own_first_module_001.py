#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import (aboslute_import , division)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleMenu


def save_data(mod):
    raise NOTImplementedError

def main():
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/xxx")
        )
    )
    save_data(mod)


if __name__ == "__main__":
    main()
