#!/usr/bin/env python

from __future__ import with_statement

import sys

from setuptools import setup, find_packages

#with open('README.rst') as f:
#    readme = f.read()

long_description = """
Tivan
"""

install_requires = [
    'Django==1.8.6',
    'djangorestframework==3.3.1',
    'mysqlclient==1.3.7',
    'requests~=2.8'
]

setup(
    name='tivan',
    version='0.0.0a0',
    description='tivan',
    long_description=long_description,
    author='wilypomegranate',
    author_email='wilypomegranate@users.noreply.github.com>',
    #url='',
    packages=find_packages(),
    test_suite='py.test',
    tests_require=['pytest'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'motion_scripts = tivan.motion_scripts.__main__:main',
        ]
    },
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Topic :: System :: Systems Administration',
    ],
)
