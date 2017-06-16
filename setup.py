#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'gtts',
    'pygame'
]

test_requirements = [
	'tox',
	'flake8'
]

setup(
    name='vox',
    version='0.0.1',
    description="Simple Text to Voice API for Python and Command Line",
    long_description=readme + '\n\n' + history,
    author="Muhammad Rizwan",
    author_email='m.rizwan_47@yahoo.com',
    url='https://github.com/mrizwan47/vox',
    packages=[
        'vox',
    ],
    package_dir={'vox': 'vox'},
    install_requires=requirements,
    license="MIT license",
    keywords='vox text-to-speech',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
