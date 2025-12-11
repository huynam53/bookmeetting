import os

loggers = {
    'app': {
        'handlers': ['app'],
        'level': 'INFO',
        'propagate': False,
    },
}

if os.environ.get('DEBUG') == 'True' and os.environ.get('DB_SHOW_SQL') == 'True':
    loggers['django.db.backends'] = {
        'handlers': ['db'],
        'level': 'DEBUG',
        'propagate': False,
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'app': {
            'format': "%(asctime)s,%(msecs)03d | %(levelname)s | DMV | AppLog | dms-api"
                      "| %(thread)d | %(name)s | %(message)s",
            'datefmt': "%Y-%m-%dT%H:%M:%S"
        },
        'db': {
            'format': "%(asctime)s,%(msecs)03d | %(levelname)s %(message)s",
            'datefmt': "%Y-%m-%dT%H:%M:%S"
        },
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'app',
            'stream': "ext://sys.stdout"
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'db',
            'stream': "ext://sys.stdout"
        },
    },
    'loggers': loggers
}
