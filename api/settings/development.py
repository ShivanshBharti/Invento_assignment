

from .base import *

DEBUG = True




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'apiDev',
        'USER':'postgres',
        'PASSWORD':'shivansh',
        'HOST':'localhost',
    }
}