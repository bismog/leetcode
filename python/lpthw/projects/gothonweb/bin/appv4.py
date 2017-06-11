#!/usr/bin/env python
# -*- coding:utf-8 -*-

import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
        # import pdb;pdb.set_trace()
        # return render.hello_form()
        return render.hello_form_laid_out()

    def POST(self):
        form = web.input(name='Nobody', greet=None)
        # import pdb;pdb.set_trace()
        if form.greet:
            greeting = "%s %s" % (form.greet, form.name)
            # greeting = "Hello %s" % form.name
            # greeting = "Hello World"
            # return greeting
            # return render.index(greeting = greeting)
            return render.index_laid_out(greeting = greeting)
        else:
            return "ERROR: greet is required."

if __name__ == "__main__":
    app.run()

