#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from setuptools import setup, find_packages
# import setuptools


def get_version() -> str:
    # https://packaging.python.org/guides/single-sourcing-package-version/
    init = open(os.path.join("onpolicy", "__init__.py"), "r").read().split()
    return init[init.index("__version__") + 2][1:-1]

setup(
    name="onpolicy",  # Replace with your own username
    version="1.0.0",
    description="on-policy algorithms of marlbenchmark",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    author="zoeyuchao",
    author_email="zoeyuchao@gmail.com",
    packages=find_packages(),
    license="MIT License",
    keywords="multi-agent reinforcement learning platform pytorch",
)
