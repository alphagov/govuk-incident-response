import os

import dj_database_url
from response.slack.client import SlackClient

from .common import *


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['govuk-incident-response.cloudapps.digital']

DATABASES = {'default': dj_database_url.config()}

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_URL = f'https://{ALLOWED_HOSTS[0]}'

SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
SLACK_CLIENT = SlackClient(SLACK_TOKEN)

INCIDENT_CHANNEL_ID = os.environ['INCIDENT_CHANNEL_ID']
