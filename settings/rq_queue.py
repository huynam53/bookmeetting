import os

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDIS_URL'),
        'DEFAULT_TIMEOUT': 500
    },
    'approval_notice': {
        'URL': os.getenv('REDIS_URL'),
        'DEFAULT_TIMEOUT': 500
    }
}