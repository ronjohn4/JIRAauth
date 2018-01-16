from flask import json
import requests

class JIRAhandler():
    _JiraSession = None
    _JiraBaseUrl = None

    def __init__(self, JiraBaseUrl):
        self._JiraSession =  requests.session()  # NOT a Flask session
        self._JiraBaseUrl = JiraBaseUrl
        self._JiraSession.auth = None

    # gather JIRA information about the current user and format
    def user(self):
        error = None
        r = self._JiraSession.get(self._JiraBaseUrl + '/rest/api/2/myself')

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
            error = 'There was a problem with the JIRA call, status_code=' + str(r.status_code)

        return r.text, formatted, error

    # authenticate the specified auth against JIRA
    def auth(self, s, auth):
        self._JiraSession.auth = auth
        r = self._JiraSession.get(self._JiraBaseUrl + '/rest/auth/1/session')
        if r.status_code != 200:
            self._JiraSession.auth = None
            s['isAuthenticated'] = False
        else:
            s['isAuthenticated'] = True
        return r.status_code == 200

    def isAuth(self):
        return self._JiraSession.auth != None

    def logout(self, s):
        self._JiraSession.auth = None
        s['isAuthenticated'] = False



