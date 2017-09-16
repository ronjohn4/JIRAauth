#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging

from flask import Flask, render_template, request, redirect, url_for, session, json
# from flask import make_response, flash
from functools import wraps
import requests

app = Flask('JIRAauth')

# todo - test that JiraSession isn't shared with all users
# This is NOT the Flask session
JiraSession = requests.session()
JiraSession.cookies['JIRA_URL'] = 'https://levelsbeyond.atlassian.net'
JiraSession.auth = None

# secret_key is used for flash messages
app.config.update(dict(
    SECRET_KEY='development key goes here, should be complex'
))


def Auth():
    r = JiraSession.get(JiraSession.cookies['JIRA_URL'] + '/rest/auth/1/session')
    return r.status_code == 200


def authenticated_resource(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if JiraSession.auth:
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


# sample route showing how to use JiraSession to make additional calls to JIRA
# JIRA documentation for this API is here:
#     https: // docs.atlassian.com / jira / REST / cloud /  # api/2/myself-getUser
@app.route('/jirauserinfo/')
@authenticated_resource
def jirauserinfo():
    error = None
    r = JiraSession.get(JiraSession.cookies['JIRA_URL'] + '/rest/api/2/myself')

    formatted = {}
    if r.status_code == 200:
        json_return = json.loads(r.text)
        formatted['self'] = json_return['self']
        formatted['key'] = json_return['key']
        formatted['name'] = json_return['name']
        formatted['displayName'] = json_return['displayName']
        formatted['active'] = json_return['active']
        formatted['timeZone'] = json_return['timeZone']
    else:
        error = 'There was a problem with the JIRA call, status_code='+r.status_code

    return render_template('jirauserinfo.html', response=r.text, formatted=formatted, error=error)


@app.route('/unsecure/')
def unsecure():
    return render_template('unsecure.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        JiraSession.auth = (request.form['username'], request.form['password'])
        if Auth():
            session['isAuthenticated'] = True
            return redirect(session["wants_url"])
        else:
            session['isAuthenticated'] = False
            JiraSession.auth = None
            error = 'Invalid Credentials. Please try again.'
    else:
        # when user specifically selects login from any page, want to go back to that page
        session["wants_url"] = request.referrer
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    JiraSession.auth = None
    session['isAuthenticated'] = False
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
