#!/usr/bin/env python
# -*- coding:utf-8 -*-


from __future__ import print_function

import urllib2

import taskflow.engines
from taskflow.patterns import unordered_flow as uf
from taskflow import task


def flow_watch(state, details):
    print('Flow state:{}'.format(state))
    print('Flow details:{}'.format(details))

def task_watch(state, details):
    print('Task state:{}'.format(state))
    print('Task details:{}'.format(details))

def fetch(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    return response.getcode()


class GoogleFetch(task.Task):
    default_provides = 'g-fetch'
    def execute(self, google_url, *args, **kwargs):
        status_code = fetch(google_url)
        print('Google Response Code: {}'.format(status_code))

    def revert(self, google_url, *args, **kargvs):
        print('Magically Reverting the Google Call!')


class AmazonFetch(task.Task):
    default_provides = 'a-fetch'
    def execute(self, amazon_url, *args, **kwargs):
        status_code = fetch(amazon_url)
        print('Amazon Response Code: {}'.format(status_code))

    def revert(self, amazon_url, *args, **kargvs):
        print('Magically Reverting the Amazon Call!')

if __name__ == "__main__":
    flow = uf.Flow('simple-unordered-listen').add(
        GoogleFetch(),
        AmazonFetch()
    )

    # taskflow.engines.run(flow, store=dict(google_url='http://baidu.com',
    #                                       amazon_url='http://www.taobao.com'))

    engine = taskflow.engines.load(flow,
        store = dict(
            google_url = 'http://baidu.com',
            amazon_url = 'HELLO!http://www.taobao.com'))
    engine.notifier.register('*', flow_watch)
    # engine.task_notifier.register('*', task_watch)
    try:
        engine.run()
    except urllib2.URLError:
        print('I think the URL is bad in one of the tasks...')
    except Exception as ex:
        print(ex.message)
