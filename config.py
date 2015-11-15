import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '\xa4\x12%W\x01\xba9\x1e\xea\xab\x02\x8e\x03(\xc8,L\x8a\xd2\x97\xdes\x91\x01'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = False
