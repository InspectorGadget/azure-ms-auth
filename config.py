import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'wwqeewrrteyrtrye234')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    AUTHORITY = os.environ.get('AUTHORITY')
    SCOPE = ["User.ReadBasic.All"]
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
