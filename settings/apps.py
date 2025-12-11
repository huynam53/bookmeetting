#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  apps.py
#

# Application definition

INSTALLED_APPS = (
    'rest_framework',
    'django_filters',  # for filtering rest endpoints
    'storages',
    # 'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'app.products',
    'app.orders',
    'app.promotions',
    'app.feedback',
)
