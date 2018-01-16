from JIRAhandler import JIRAhandler
import json

class JIRAhandlerauth(JIRAhandler.JIRAhandler):
    """JIRAhandlerauth returns simple user information from JIRA.

    JIRAhandlerauth subclasses JIRAhandler that manages JIRA authentication and session.

    Methods:
        User    Returns the JIRA user information for the currently authenticated user.
    """

    def __init__(self, JiraBaseUrl):
        super(self.__class__, self).__init__(JiraBaseUrl)


    # gather JIRA information about the current user and format
    def User(self):
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
