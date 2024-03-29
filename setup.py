# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = []

config = {
    "version": "0.1",
    "name": "eprint",
    "url": "https://github.com/jakeogh/eprint",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "print() alias that writes to sys.stderr",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"eprint": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "eprint=eprint.eprint:cli",
        ],
    },
}

setup(**config)
