#!/usr/bin/env python

import os
from setuptools import setup, find_packages

with open(os.path.join( 'one_lin3r', 'core', 'resources', 'version.txt')) as f:
    version = f.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='one-lin3r',
    version=version,
    author='Karim Shoair (D4Vinci)',
    author_email="karim.shoair@pm.me",
    description='One-Lin3r is simple modular and light-weight framework gives you all the one-liners that you will need while penetration testing (Windows, Linux, macOS or even BSD systems) or hacking generally with a lot of new features to make all of this fully automated (ex: you won\'t even need to copy the one-liners).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/D4Vinci/One-Lin3r',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'terminaltables',
        'pyperclip',
        'prompt_toolkit',
        'win_unicode_console;platform_system=="Windows"',
        'colorama;platform_system=="Windows"',
    ],
    classifiers=[
        "Topic :: Security",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Other Audience",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'one-lin3r = one_lin3r.main:main',
        ],
    },
)
