#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def get_version():
    with open("hostingde/__version__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="python-hostingde",
    version=get_version(),
    description="Interact with HostingDe API",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Benedict Becker",
    author_email="benedict.becker93@gmail.com",
    license="LGPLv3",
    url="https://github.com/becelot/python-hostingde",
    packages=find_packages(exclude=["docs*", "tests*"]),
    install_requires=[
        "requests>=2.25.1",
        "marshmallow==3.10.0",
        "marshmallow-dataclass==8.3.1",
        "marshmallow-enum==1.5.1",
        "urllib3~=1.26.3",
        "responses~=0.13.1"
    ],
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
