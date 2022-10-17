#!/usr/bin/env python
"""
@author: metalcorebear
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentimizer",
    version="1.0",
    author="metalcorebear",
    author_email="mark.mbailey@gmail.com",
    description="Sentimizer will measure sentiment around specific entities within text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metalcorebear/sentimizer",
    packages=setuptools.find_packages(),
    install_requires=['nltk', 'spacy', 'NRCLex'],
    include_package_data=True,
    py_modules=["sentimizer"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)