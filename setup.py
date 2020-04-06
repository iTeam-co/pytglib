#!/usr/bin/env python
import setuptools
from sys import argv
from generate.api import generator

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install"]:
     generator.start()

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='Pytglib',
    version='0.4',
    description='Python library to help you build your own Telegram clients',
    author='iTeam',
    author_email='co.amirh@gmail.com',
    url='https://github.com/iTeam-co/python-telegram',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'pytglib': [
            'lib/darwin/*',
            'lib/linux/*',
        ],
    },
)
