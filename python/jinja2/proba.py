#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://pythonadventures.wordpress.com/2014/02/25/jinja2-example-for-generating-a-local-file-using-a-template/

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape = False,
    loader = FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks = False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = 'output.html'
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    context = {
        'urls': urls
    }

    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)


def main():
    create_index_html()


if __name__ == '__main__':
    main()
