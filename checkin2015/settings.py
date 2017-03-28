"""
Django production settings for checkin2015 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from envs.common import *


# Private settings
if ON_OPENSHIFT:
    DB_NAME = os.environ['OPENSHIFT_APP_NAME']
    DB_USER = os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']
    DB_PASSWORD = os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
    DB_HOST = os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
    DB_PORT = os.environ['OPENSHIFT_POSTGRESQL_DB_PORT']
else:
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

from datetime import date
COMPETITION_START_DATE = date(2017, 4, 24)
COMPETITION_END_DATE = date(2017, 10, 30)
