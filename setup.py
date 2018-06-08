#!/usr/bin/env python

import os
from setuptools import setup, find_packages

with open(os.path.join('One_Lin3r', 'Core', 'resources', 'version.txt')) as f:
    version = f.read().strip()

setup(name='One-Lin3r',
    version=version,
    description='One-Lin3r is simple and light-weight framework gives you one-liners that aids in pentesting operations',
    author='Karim Shoair',
    url='https://github.com/D4Vinci/One-Lin3r',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'terminaltables',
        'readline;platform_system!="Windows"',
        'pyreadline;platform_system=="Windows"',
        'win_unicode_console;platform_system=="Windows"',
        'colorama;platform_system=="Windows"',
    ],
    entry_points={
        'console_scripts': [
            'one-lin3r = One_Lin3r.main:main',
        ],
    },
)
