"""This file defines how dump2json is installed in a python environment.
"""
import setuptools

setuptools.setup(
    name='pytest-dump2json',
    version='0.1.0',
    py_modules=['dump2json'],
    install_requires=['pytest'],
    test_suite='test',
    entry_points = {
        'pytest11': [
            'pytest-dump2json = dump2json',
        ]
    },
)
