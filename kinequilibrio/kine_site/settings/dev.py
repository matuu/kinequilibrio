from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ylmwspp@q(56i97ar%gsmlcqe!$*5+r^zhd@7*%po1kp4c0q4$'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + (
    'django_extensions',
    'template_debug',
    'debug_toolbar',
)
try:
    from .local import *
except ImportError:
    pass

DEBUG = True
