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

PROJECT_APPS = ('pretty_times',)

INSTALLED_APPS = PROJECT_APPS

try:
    import django_jenkins

    INSTALLED_APPS = INSTALLED_APPS + ('django_jenkins',)
    JENKINS_TASKS = (
        'django_jenkins.tasks.django_tests',
        'django_jenkins.tasks.run_pylint',
        'django_jenkins.tasks.run_pep8',
        'django_jenkins.tasks.run_pyflakes',
        'django_jenkins.tasks.with_coverage',
    )

except ImportError:
    pass