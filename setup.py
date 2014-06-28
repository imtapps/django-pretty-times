from setuptools import find_packages
from distutils.core import setup

setup(
    name="django-pretty-times",
    version='0.2.0',
    author="imtapps",
    author_email="imtapps@apps-system.com",
    description="pretty_times provides django template helpers for the py-pretty library.",
    long_description=file('README.rst', 'r').read(),
    url="http://github.com/imtapps/django-pretty-times",
    packages=find_packages(exclude=['example']),
    install_requires=file('requirements/base.txt').read().split("\n"),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
