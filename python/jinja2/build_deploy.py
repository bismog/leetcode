#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape = False,
    # loader = FileSystemLoader(os.path.join(PATH, 'templates')),
    loader = FileSystemLoader(PATH),
    trim_blocks = False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def build_deploy():
    fname = 'output_deploy.yaml'
    context = {
        'baremetal_csv_file': '/tmp/foo_csv_file'
    }

    with open(fname, 'w') as f:
        html = render_template('deploy.yaml', context)
        f.write(html)

def main():
    build_deploy()


if __name__ == '__main__':
    main()

