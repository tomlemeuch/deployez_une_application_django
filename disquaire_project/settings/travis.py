"""
Django settings for disquaire_project project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from . import *





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'disquaire',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''

    }
}
