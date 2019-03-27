#!/usr/bin/env python
from distutils.core import setup
from sys import argv
from generate.api import generator

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install"]:
    generator.start()

setup(
    name='python-telegram',
    version='0.1',
    description='Python library to help you build your own Telegram clients',
    author='Alexander Akhmetov',
    author_email='me@aleks.sh',
    url='https://github.com/alexander-akhmetov/python-telegram',
    packages=[
        'telegram',
    ],
    package_data={
        'telegram': [
            'lib/darwin/*',
            'lib/linux/*',
        ],
    },
)
