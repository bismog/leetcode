#!/usr/bin/env python
#-*- coding:utf-8 -*-

# app/__init__.py

# existing import remains

from flask import request, jsonify, abort
from flask import Flask


bucket = {
    'id': 12345,
    'name': 'badluck',
    'date_created': '2017-4-1',
    'date_modified': '2017-8-8'
}

app = Flask(__name__)

# def create_app():

@app.route('/bucket/', methods='GET')
def get():
    result = {
        'id': bucket['id'],
        'name': bucket['name'],
        'date_created': bucket['date_created'],
        'date_modified': bucket['date_modified']
    }
    response = jsonify(results)
    response.status_code = 200
    return response

# return app

if __name__ == "__main__":
 #    app = create_app()
    app.run(debug=True)

