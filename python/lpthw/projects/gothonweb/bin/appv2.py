#!/usr/bin/env python
# -*- coding:utf-8 -*-

import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = "Hello World"
        #return greeting
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()

