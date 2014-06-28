# rules lives in a directory above our example
# app so we need to make sure it is findable on our path.
import sys
from os.path import abspath, dirname, join
parent = abspath(dirname(__file__))
grandparent = abspath(join(parent, '..'))
for path in (grandparent, parent):
    if path not in sys.path:
        sys.path.insert(0, path)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example.db',
    }
}

USE_I18N = True
LANGUAGE_CODE = 'en'

PROJECT_APPS = ('pretty_times',)

INSTALLED_APPS = ('django_nose', ) + PROJECT_APPS

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SECRET_KEY = 'abc123'
