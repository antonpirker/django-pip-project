#!/usr/bin/env python3
import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()


setup(
    version='0.2.0',
    name='pipinator',
    description='Example Project to show how to package a Django project for pip and PyPI',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pipinator = pipinator.manage:main',
        ],
    },
    install_requires=[
        'Django==2.0.2',
        'easy-thumbnails==2.5',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
    ],
    author='Anton Pirker',
    author_email='anton@ignaz.at',
    url='https://github.com/antonpirker/django-pip-project',
    keywords=['django'],
)