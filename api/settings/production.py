from .base import *


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'apiProd',
        'USER':'postgres',
        'PASSWORD':'shivansh',
        'HOST':'localhost',
    }
}

