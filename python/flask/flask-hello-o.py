#!flask/bin/python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/user/<username>')
def user(user):
    return "Hello, %s!" % username

#if __name__ == '__main__':
#    app.run(debug=True)

with app.test_request_context():
    #print url_for('')
    print url_for('user',username = 'juxicn')
    #print url_for('xxx',attr = 'length')
