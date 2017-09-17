#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging

from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import requests
from JIRAhandler import JIRAhandler

app = Flask('JIRAauth')
JiraSession = requests.session()  #NOT a Flask session
JiraHandle = JIRAhandler(JiraSession, 'https://levelsbeyond.atlassian.net')

# secret_key is used for flash messages
app.config.update(dict(
    SECRET_KEY='development key goes here, should be complex'
))


# decorator used to secure Flask routes
def authenticated_resource(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if JiraHandle.isAuth():
            return f(*args, **kwargs)
        else:
            session["wants_url"] = request.url
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


@app.route('/logout')
def logout():
    JiraHandle.logout(session)
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if JiraHandle.auth(session, (request.form['username'], request.form['password'])):
            return redirect(session["wants_url"])
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


# sample route showing how to make additional calls to JIRA
@app.route('/jirauserinfo/')
@authenticated_resource
def jirauserinfo():
    response, formatted, error = JiraHandle.user()
    return render_template('jirauserinfo.html', response=response, formatted=formatted, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5003)
