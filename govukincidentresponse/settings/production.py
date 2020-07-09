import os

import dj_database_url

from .common import *


SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {'default': dj_database_url.config()}

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_URL = os.environ['SITE_URL']

SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']

INCIDENT_CHANNEL_ID = os.environ['INCIDENT_CHANNEL_ID']
INCIDENT_BOT_ID = os.environ['INCIDENT_BOT_ID']