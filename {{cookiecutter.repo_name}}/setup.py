#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.hogarthww.prv/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="PROPRIETARY",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Private :: Do Not Upload',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
