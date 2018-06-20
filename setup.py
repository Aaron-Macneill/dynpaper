#!/usr/bin/env python3

import os
import sys

from setuptools import setup

# Dynamically calculate the version based on django.VERSION.
version = __import__('dynpaper').get_version()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='Dynpaper',
    version=version,
    url='https://www.github.com/oddproton/dynpaper',
    author='Stelios Tymvios',
    author_email='stelios.tymvios@icloud.com',
    description=('A dynamic wallpaper setter inspired by MacOS Mojave'),
    license='BSD 3-Clause "New" or "Revised" License',
    py_modules=['dynpaper'],
    entry_points={
        "console_scripts": [
            "dynpaper = dynpaper:main"
        ]
    },
)
