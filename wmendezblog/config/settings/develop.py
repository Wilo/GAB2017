from .common import *

DEBUG = True

THIRD_PARTY_APPS = [
    'django_extensions',
    'werkzeug'
]

INSTALLED_APPS += THIRD_PARTY_APPS

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

