import os


class Config(object):
    MONGODB_SETTINGS = {
        'db': os.environ['MONGODB_DATABASE'],
        'host': os.environ['MONGODB_HOSTNAME'],
        'port': 27017
    }
    SECRET_KEY = os.environ.get('SECRET_KEY')
