# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_mail import Mail
from flask_mail import Message
from flask_bootstrap import Bootstrap
from threading import Thread

app = Flask(__name__)
bootstrap = Bootstrap(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flask]'
app.config['FLASK_MAIL_SENDER'] = 'Flask Admin<s142062410122@163.com>'
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr


@app.route('/')
def index():
    send_mail(app.config['FLASK_ADMIN'], 'New User',
              'mail/new_user', user='hello')
    return render_template('mail/new_user.html', user='hi')


if __name__ == '__main__':
    app.run(debug=True)
