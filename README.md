# JIRA Auth
#### Python/Flask webapp authenticating against JIRA

JIRA Auth is a sample project using Flask and requests to authenticate and pull data from JIRA.  This project does not use Flask-Login or JIRA packages.

**Flask-Login** isn't used because the purpose is to authenticate against JIRA, not to manage users.  This project authenticates pages with a decorator the same as Flask-Login.

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

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
You need Python 3.4 or later and the latest version of virtualenv to create the runtime environment.  

```
$ sudo apt-get install python3 python3-pip
$ sudo pip install virtualenv

```

### Installing

The steps below will clone a copy of the code to your local machine, create a virtual environment and setup any dependencies.

```
$ git clone https://github.com/ronjohn4/JIRAauth  
$ virtualenv JIRAauth --python=python3
$ cd JIRAauth
$ source ./bin/activate ('scripts\activate' on Windows)
(JIRAauth)$ python setup.py install
```

### Running

The command below will start the app in your default webserver on port 5003 (this can be changed in the code).

```
$ python JIRAauth.py
```

The address where the app is running will be displayed on the command line.  Simply navigate to this address in your browser.
Use a CTRL+C to stop the app.