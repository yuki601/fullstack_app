from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_staging',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host.docker.internal',
        'PORT': '53306',
        'ATOMIC_REQUESTS': True
    }
}