import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        b'0vM|\x1b\xde{\x99F\xca\x17j0a\xb4\xf6'

    MONGODB_SETTINGS = {
        'db': 'UTA_Enrollment'
    }
