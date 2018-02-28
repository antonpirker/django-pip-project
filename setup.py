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
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
    ],
    author='Anton Pirker',
    author_email='anton@ignaz.at',
    url='https://github.com/antonpirker/django-pip-project',
    keywords=['django'],
)