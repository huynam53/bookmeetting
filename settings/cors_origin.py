#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  cors_origin.py
#
#
#  Created by thang doan on 04/02/2024.

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
    'Access-Control-Allow-Methods: *',
)
CORS_ALLOW_METHODS = ['*']
CORS_ALLOW_HEADERS = ['*']
