"""
This file contain settings for Django REST framework
refrence: http://www.django-rest-framework.org/api-guide/settings/
"""
import os

APPS_THROTTLE_GET_REQUEST = os.getenv("APPS_THROTTLE_GET_REQUEST")
APPS_THROTTLE_POST_REQUEST = os.getenv("APPS_THROTTLE_POST_REQUEST")
APPS_THROTTLE_PUT_REQUEST = os.getenv("APPS_THROTTLE_PUT_REQUEST")
APPS_THROTTLE_PATCH_REQUEST = os.getenv("APPS_THROTTLE_PATCH_REQUEST")
APPS_THROTTLE_DELETE_REQUEST = os.getenv("APPS_THROTTLE_DELETE_REQUEST")
APPS_THROTTLE_DURATION_REQUEST = os.getenv("APPS_THROTTLE_DURATION_REQUEST")

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': (
        'configs.throttle.RequestMethodThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user_get': '%s/%s' % (APPS_THROTTLE_GET_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_post': '%s/%s' % (APPS_THROTTLE_POST_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_put': '%s/%s' % (APPS_THROTTLE_PUT_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_patch': '%s/%s' % (APPS_THROTTLE_PATCH_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_delete': '%s/%s' % (APPS_THROTTLE_DELETE_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_options': '%s/%s' % (APPS_THROTTLE_DELETE_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_head': '%s/%s' % (APPS_THROTTLE_DELETE_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
    },
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # If you want to remove django.contrib.auth, set UNAUTHENTICATED_USER is None
    # https://github.com/encode/django-rest-framework/issues/3262
    # 'UNAUTHENTICATED_USER': None,
}