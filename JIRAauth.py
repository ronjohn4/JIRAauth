# Ron Johnson
# 9/9/2017
#
# Jira Basic Authentication

class JiraBasicAuth():
    username = None
    __password = None
    __session = None
    isAuthenticated = None

    def __init__(self, session):
        self.__session = session
        self.isAuthenticated = self.Auth()

    def Auth(self, username=None, password=None):
        if username is not None:
            self.username = username
            self.__password = password
            self.__session.auth = (self.username, self.__password)

        url = 'https://levelsbeyond.atlassian.net/rest/auth/1/session'
        r = self.__session.get(url)
        return r.status_code == 200


    def Logout(self):
        self.username = None
        self.__password = None
        self.__session.auth = (self.username, self.__password)

        url = 'https://levelsbeyond.atlassian.net/rest/auth/1/session'
        r = self.__session.get(url)
        return r.status_code != 200
