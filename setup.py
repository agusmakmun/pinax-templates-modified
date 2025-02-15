import os
import sys
from setuptools import find_packages, setup

VERSION = "3.0.1"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-templates.svg
    :target: https://pypi.python.org/pypi/pinax-templates/

===============
Pinax Templates
===============

.. image:: https://img.shields.io/pypi/v/pinax-templates.svg
    :target: https://pypi.python.org/pypi/pinax-templates/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-templates.svg
    :target: https://circleci.com/gh/pinax/pinax-templates
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-templates.svg
    :target: https://codecov.io/gh/pinax/pinax-templates
.. image:: https://img.shields.io/github/contributors/pinax/pinax-templates.svg
    :target: https://github.com/pinax/pinax-templates/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-templates.svg
    :target: https://github.com/pinax/pinax-templates/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-templates.svg
    :target: https://github.com/pinax/pinax-templates/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-templates/

\

``pinax-templates`` provides semantically-correct templates for use with Pinax apps.


Supported Pinax Apps
--------------------

* django-user-accounts
* pinax-announcements
* pinax-blog
* pinax-cohorts
* pinax-documents
* pinax-invitations
* pinax-likes
* pinax-notifications
* pinax-strip


Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 3.2 | 3.5 | 3.6 | 4.2 |
+=================+=====+=====+=====+=====+
|  3.2            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  4.2            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()


setup(
    author="Pinax Team",
    author_email="team@pinaxprojects.com",
    description="semantic templates for pinax apps",
    name="pinax-templates-modified",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-templates/",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=3.2",
        "django-bootstrap-form>=3.0.0"
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
