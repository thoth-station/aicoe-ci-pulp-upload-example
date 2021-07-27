"""Setup for hello world module."""

import os

from setuptools import setup
from pathlib import Path


def get_install_requires():
    """Get requirements from requirements.txt."""
    with open("requirements.txt", "r") as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(" ", maxsplit=1)[0] for req in res if req]


def get_version():
    """Get package version."""
    with open(os.path.join("aicoe", "hello_world", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


VERSION = get_version()
setup(
    name="aicoe-hello-world",
    version=VERSION,
    description="Hello World module of AICoE",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Harshad Reddy Nalla",
    author_email="hnalla@redhat.com",
    license="GPLv3+",
    packages=["aicoe.hello_world"],
    zip_safe=False,
    install_requires=get_install_requires(),
    command_options={
        "build_sphinx": {
            "version": ("setup.py", VERSION),
            "release": ("setup.py", VERSION),
        }
    },
)
