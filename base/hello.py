# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    response = make_response('<h1>this docunet carries a cookies!</h1>', 200)
    user_agent = request.headers.get('User-Agent')
    response.set_cookie('UA', user_agent)
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name, 400


@app.route('/post/<int:id>')
def post_new(id):
    user = None
    if not user:
        abort(404)
    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
