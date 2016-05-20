"""
Django settings for checkin2015 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# from checkin2015.settings import *

import os
import django.conf.global_settings as DEFAULT_SETTINGS
from django.conf import settings
from django.conf.urls.static import static

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
SECRET_RECAPTCHA_KEY = os.getenv('SECRET_RECAPTCHA_KEY', '')

# Mandrill (https://mandrillapp.com/) is used to email checkin confirmations
MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY', '')

# MapQuest
MAPQUEST_API_KEY = os.getenv('MAPQUEST_API_KEY', '')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u+%bt4*6s_n4s!6va0jm214_%!+djw+dczi+cpi2)vl!mbqot%'

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
    DEBUG = bool(os.environ.get('DEBUG', False))
    if DEBUG:
        print('WARNING: The DEBUG environment is set to True.')
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'survey',
    'leaderboard',
    'retail',
    'smart_selects',  # for the subteams dropdown functionality
    'django.contrib.humanize'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'checkin2015.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# Templates
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
    '/static/'
)


WSGI_APPLICATION = 'checkin2015.wsgi.application'

# Sessions!
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 31 * 7  # length of the challenge in seconds?

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "test/test_db_checkin.db",
        'ATOMIC_REQUESTS': True,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Email settings
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = MANDRILL_API_KEY
EMAIL_HOST_USER = 'jkatzchristy@gogreenstreets.org'

USE_DJANGO_JQUERY = False
JQUERY_URL = 'static/libs/jquery-1.11.0.min.js'