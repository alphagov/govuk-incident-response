import os

from .common import *


SECRET_KEY = '&sr(f(17t^wrlx)d01j2zbu_8zp2c@bag=t_zky9h!8*j^g-xm'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

SITE_URL = os.environ.get('SITE_URL', 'http://localhost:8000')

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')

INCIDENT_CHANNEL_ID = os.environ.get('INCIDENT_CHANNEL_ID')
INCIDENT_BOT_ID = os.environ.get('INCIDENT_BOT_ID')
