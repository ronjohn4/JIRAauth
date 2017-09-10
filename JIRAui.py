#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging

from flask import Flask, render_template, flash, request, make_response, redirect, url_for
from JIRAauth import JiraBasicAuth
from functools import wraps
import requests


app = Flask('JIRAauth')
app.config['JIRAroot'] = 'https://levelsbeyond.atlassian.net'
s = requests.session()
# s.auth = ('rjohnson', 'Miter9le')


# secret_key is used for flash messages
app.config.update(dict(
    SECRET_KEY='development key'
))


def authenticated_resource(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if JiraBasicAuth(s).Auth():
            return f(*args, **kwargs)
        return redirect(url_for('login'))

    return decorated


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/secure/')
@authenticated_resource
def secure():
    return render_template('secure.html')


@app.route('/unsecure/')
def unsecure():
    return render_template('unsecure.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if JiraBasicAuth(s).Auth(request.form['username'], request.form['password']):
            return redirect(url_for('issues'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('issues'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
