# JIRA Auth
#### Python/Flask webapp authenticating against JIRA

JIRA Auth is a sample project using Flask and requests to authenticate and pull data from JIRA.  This project does not use Flask-Login or JIRA packages.

**Flask-Login** isn't used because the purpose is to authenticate against JIRA, not to managed users.  This project authenticates pages with a decorator the same as Flask-Login.

**JIRA** (the package) isn't used because I wanted to call any JIRA API and basic auth (which is simple) is being used.

JIRA Auth is a sample project showing how to:
- **Authenticate** users against a JIRA cloud instance.
- **Enforce** page level permissions using a route decorator.  This is the same as Flask-Login but validating the user is against JIRA.
- Make **subsequent calls to JIRA** for additional data.  In this sample

Sample pages are:
- **Home**
- **Unsecure** is a blank page that displays for anyone
- **Secure** is a blank page requiring authentication before being displayed
- **JIRA User Info** pulls some basic user info from JIRA.
- **Logon/Logoff** link on the right.  Switches depending on if the current user is authenticated.

The goal is to be as simple and clear as possible.
