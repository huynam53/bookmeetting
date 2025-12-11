#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  database.py
#
#
#  Created by thang doan on 04/02/2024.

import os
import dj_database_url
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=int(os.getenv("POSTGRES_CONN_MAX_AGE")),
            engine='django_tenants.postgresql_backend'
        )
}
