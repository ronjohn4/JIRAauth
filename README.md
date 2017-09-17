# JIRA Auth

JIRA Auth is a sample project using Flask and requests to authenticate and pull data from JIRA.  This project does not use Flask-Login or JIRA packages.

**Flask-Login** isn't used because the purpose is to authenticate against JIRA, not to manage users.  This project does authenticate pages with a decorator the same as Flask-Login.

**JIRA** (the package) isn't used because I wanted to call any JIRA API and basic auth (which is simple) is being used.

JIRA Auth is a sample project showing how to:
- **Authenticate** users against JIRA cloud
- **Enforce** page level permissions using a route decorator
- Make **subsequent calls to JIRA** for additional data

The goal is to be as simple and clear as possible.