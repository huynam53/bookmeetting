#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  templates.py
#
#
#  Created by thang doan on 04/02/2024.

import os
from .base import BASE_DIR


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
