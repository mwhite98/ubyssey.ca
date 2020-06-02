# Deployment settings

import os

# Two Scoops of Django, p. 47: "For the singular case of Django setting modules we want to override all the namespace"
# Therefore the below "import *" is correct
from .base import *

SECRET_KEY = 'TEMP-KEY'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['ubyssey.events',]

STATICFILES_DIRS += (
    os.path.join(os.path.dirname(__file__), 'static/dist'),
)

STATIC_ROOT = '/home/travis/build/ubyssey/ubyssey.ca/gcs/static'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'