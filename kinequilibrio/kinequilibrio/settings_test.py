__author__ = 'm4tuu'
from kinequilibrio.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
SOUTH_TESTS_MIGRATE = False

# Special folder to contain test media. It gets cleaned up after tests run (not
# implemented on all tests).
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../../test_media/')
