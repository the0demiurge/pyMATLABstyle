#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


readme = '\n'.join(open('README.md').readlines())

setuptools.setup(
    name='pyMATLABstyle',
    version='1.2.1',

    # Project description
    description='MATLAB style of creating numpy/sympy matrices, and a few MATLAB style functions',
    long_description=readme,
    long_description_content_type="text/markdown",

    # Author details
    author='Charles Xu',
    author_email='charl3s.xu@gmail.com',

    # Project details
    url='https://github.com/the0demiurge/pyMATLAB-style',

    # Project dependencies
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python",
        "License :: Other/Proprietary License",
        "Operating System :: Android",
        "Operating System :: iOS",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: Other OS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
    packages=setuptools.find_packages(),
)
