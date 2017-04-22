from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'blog__development',
        'USER': 'wilo@gab',
        'PASSWORD': 'SamSepiol123456',
        'HOST': 'gab.database.windows.net',
        'PORT':'1433',
        'OPTIONS':{
               'driver':'ODBC Driver 13 for SQL Server',
#              'MARS_Connection': 'True',
        }
    }
}

